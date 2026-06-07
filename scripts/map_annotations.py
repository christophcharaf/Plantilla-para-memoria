"""Map reviewer PDF annotations to highlighted text (XFDF or embedded PDF annots).

Usage:
    python scripts/map_annotations.py
        Auto-detect newest PDF/XFDF pair or PDF-only in Correcciones/

    python scripts/map_annotations.py <PDF> <XFDF>
        Map using XFDF coordinates (best highlight text quality)

    python scripts/map_annotations.py --pdf-only <PDF>
        Map using embedded PDF highlight annotations

    python scripts/map_annotations.py --pdf-only <PDF> --output Correcciones/foo.md
        Write Markdown table for agent consumption
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

import fitz

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "Correcciones"
NS = {"x": "http://ns.adobe.com/xfdf/"}
VERSION_RE = re.compile(r"_V(\d+)", re.IGNORECASE)


@dataclass
class AnnotationRow:
    index: int
    page: int
    comment: str
    highlighted: str


def version_key(path: Path) -> tuple[int, float]:
    match = VERSION_RE.search(path.stem)
    version = int(match.group(1)) if match else 0
    return version, path.stat().st_mtime


def autodetect_xfdf_pair() -> tuple[Path, Path]:
    pdfs = list(DEFAULT_DIR.glob("*.pdf"))
    xfdfs = list(DEFAULT_DIR.glob("*.xfdf"))
    if not pdfs or not xfdfs:
        raise SystemExit(
            f"No PDF/XFDF pair found in {DEFAULT_DIR}. "
            "Use --pdf-only or pass explicit paths."
        )

    pdfs_by_stem = {p.stem: p for p in pdfs}
    pairs: list[tuple[Path, Path, int, float]] = []
    for xfdf in xfdfs:
        pdf = pdfs_by_stem.get(xfdf.stem)
        if pdf is not None:
            vk, mt = version_key(pdf)
            pairs.append((pdf, xfdf, vk, mt))

    if not pairs:
        raise SystemExit(
            f"No matching PDF/XFDF basename pairs in {DEFAULT_DIR}."
        )

    pairs.sort(key=lambda item: (item[2], item[3]), reverse=True)
    return pairs[0][0], pairs[0][1]


def autodetect_pdf_only() -> Path:
    pdfs = list(DEFAULT_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDF found in {DEFAULT_DIR}.")
    pdfs.sort(key=version_key, reverse=True)
    return pdfs[0]


def parse_rect(rect_str: str) -> tuple[float, float, float, float]:
    parts = [float(v) for v in rect_str.split(",")]
    return parts[0], parts[1], parts[2], parts[3]


def get_words_in_rect(page: fitz.Page, rect: tuple[float, float, float, float]) -> str:
    x1, y1, x2, y2 = rect
    page_height = page.rect.height
    pdf_y2 = page_height - y1
    pdf_y1 = page_height - y2
    clip = fitz.Rect(x1, pdf_y1, x2, pdf_y2)
    words = page.get_text("words", clip=clip)
    return " ".join(w[4] for w in words).strip()


def text_from_pdf_annot(page: fitz.Page, annot: fitz.Annot, pad: float = 2.0) -> str:
    clip = annot.rect + (-pad, -pad, pad, pad)
    text = page.get_textbox(clip).strip().replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    if len(text) < 3:
        return ""
    return text


def normalize_comment(raw: str) -> str:
    return re.sub(r"\s+", " ", raw).strip()


def truncate(text: str, max_len: int = 60) -> str:
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def collect_from_xfdf(pdf_path: Path, xfdf_path: Path) -> list[AnnotationRow]:
    doc = fitz.open(pdf_path)
    tree = ET.parse(xfdf_path)
    root = tree.getroot()
    annots = root.find("x:annots", NS)
    if annots is None:
        return []

    rows: list[AnnotationRow] = []
    for idx, hl in enumerate(annots.findall("x:highlight", NS), 1):
        page_num = int(hl.get("page", "0"))
        rect = parse_rect(hl.get("rect", "0,0,0,0"))
        contents_el = hl.find("x:contents", NS)
        comment = normalize_comment(contents_el.text or "") if contents_el is not None else ""

        if page_num >= len(doc):
            highlighted = "(página fuera de rango)"
        else:
            highlighted = get_words_in_rect(doc[page_num], rect) or "(sin texto / ver PDF)"

        rows.append(
            AnnotationRow(
                index=idx,
                page=page_num + 1,
                comment=comment,
                highlighted=highlighted,
            )
        )
    doc.close()
    return rows


def is_reviewer_annot(annot: fitz.Annot) -> bool:
    """Include highlights and sticky-note style Text annots from the reviewer."""
    kind = annot.type[0]
    return kind in (fitz.PDF_ANNOT_HIGHLIGHT, fitz.PDF_ANNOT_TEXT)


def collect_from_pdf(pdf_path: Path) -> list[AnnotationRow]:
    doc = fitz.open(pdf_path)
    rows: list[AnnotationRow] = []
    idx = 0
    for page_num, page in enumerate(doc):
        for annot in page.annots() or []:
            if not is_reviewer_annot(annot):
                continue
            idx += 1
            comment = normalize_comment(annot.info.get("content") or "")
            highlighted = text_from_pdf_annot(page, annot) or "(sin texto / ver PDF)"
            rows.append(
                AnnotationRow(
                    index=idx,
                    page=page_num + 1,
                    comment=comment,
                    highlighted=highlighted,
                )
            )
    doc.close()
    return rows


def print_table(rows: list[AnnotationRow]) -> None:
    print(f"{'#':>3} {'Pág':>4}  {'Comentario':<55}  Texto resaltado")
    print("-" * 130)
    for row in rows:
        comment_short = truncate(row.comment, 55)
        highlighted_short = truncate(row.highlighted, 60)
        print(f"{row.index:>3}  {row.page:>3}   {comment_short:<55}  {highlighted_short!r}")


def escape_md_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def write_markdown(rows: list[AnnotationRow], pdf_path: Path, output_path: Path) -> None:
    lines = [
        f"# Correcciones revisor — {pdf_path.stem}",
        "",
        f"Fuente: `{pdf_path.name}`",
        f"Fecha exportación: {date.today().isoformat()}",
        "",
        "| # | Pág | Comentario | Texto resaltado |",
        "|---|-----|------------|-----------------|",
    ]
    for row in rows:
        lines.append(
            f"| {row.index} | {row.page} | {escape_md_cell(row.comment)} | "
            f"{escape_md_cell(row.highlighted)} |"
        )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} rows to {output_path}")


def default_output_path(pdf_path: Path) -> Path:
    stem = pdf_path.stem
    if stem.endswith("_correcciones"):
        return pdf_path.with_suffix(".md")
    return pdf_path.parent / f"{stem}_correcciones.md"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pdf",
        nargs="?",
        help="Path to annotated PDF",
    )
    parser.add_argument(
        "xfdf",
        nargs="?",
        help="Path to XFDF export (omit with --pdf-only)",
    )
    parser.add_argument(
        "--pdf-only",
        action="store_true",
        help="Read embedded PDF highlight annotations (no XFDF)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Write Markdown table to this path",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.pdf_only:
        if args.pdf:
            pdf_path = Path(args.pdf)
        else:
            pdf_path = autodetect_pdf_only()
        xfdf_path = None
    elif args.pdf and args.xfdf:
        pdf_path = Path(args.pdf)
        xfdf_path = Path(args.xfdf)
    elif args.pdf:
        parser.error("XFDF path required unless --pdf-only is set.")
    else:
        try:
            pdf_path, xfdf_path = autodetect_xfdf_pair()
        except SystemExit:
            pdf_path = autodetect_pdf_only()
            xfdf_path = None

    print(f"PDF:  {pdf_path}")
    if xfdf_path:
        print(f"XFDF: {xfdf_path}")
    else:
        print("Mode: embedded PDF annotations")
    print()

    if xfdf_path:
        rows = collect_from_xfdf(pdf_path, xfdf_path)
    else:
        rows = collect_from_pdf(pdf_path)

    if not rows:
        print("No annotations found")
        return

    print_table(rows)

    if args.output:
        write_markdown(rows, pdf_path, args.output)
    elif args.pdf_only and not args.xfdf:
        out = default_output_path(pdf_path)
        write_markdown(rows, pdf_path, out)


if __name__ == "__main__":
    main()
