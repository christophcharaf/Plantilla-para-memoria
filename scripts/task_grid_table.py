"""Tabla de avance de tareas en formato grilla original (4 tareas × 2 subceldas)."""

from __future__ import annotations

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

GREEN = "00FF00"
YELLOW = "FFFF00"
RED = "FF0000"

# (nombre, color, costo, tiempo, critico)
TASKS = [
    ("1.1 Revisión del estado del arte", GREEN, "$", "=", False),
    ("1.2 Análisis de métricas en Prometheus", GREEN, "$", "=", True),
    ("1.3 Definición de requerimientos", GREEN, "$", "=", False),
    ("1.4 Diseño preliminar del pipeline", GREEN, "$", "=", True),
    ("2.1 Recolector de métricas desde Prometheus", GREEN, "$", "=", True),
    ("2.2 Preprocesamiento y normalización", GREEN, "$", "=", True),
    ("2.3 Ingeniería de variables temporales", GREEN, "$", "=", False),
    ("2.4 Ventanas deslizantes", GREEN, "$", "=", True),
    ("2.5 Validación del pipeline", GREEN, "$", "=", False),
    ("3.1 Definición arquitectura LSTM Autoencoder", GREEN, "$", "=", True),
    ("3.2 Implementación en Keras/TensorFlow", GREEN, "$", "=", False),
    ("3.3 Preparación conjuntos train/val", GREEN, "$", "=", False),
    ("3.4 Entrenamiento y tuning", GREEN, "$", "+", True),
    ("3.5 Evaluación con métricas objetivas", GREEN, "$", "=", False),
    ("4.1 Mecanismo de alerta con umbral", GREEN, "$", "=", True),
    ("4.2 Integración con Opsgenie", GREEN, "$", "=", True),
    ("4.3 Enlaces a dashboards Grafana", GREEN, "$", "=", False),
    ("4.4 Pruebas de integración", GREEN, "$", "=", False),
    ("5.1 Validación funcional con operaciones", GREEN, "$", "=", True),
    ("5.2 Informe de resultados y validación", GREEN, "$", "=", False),
    ("5.3 Redacción memoria (1° bimestre)", GREEN, "$", "=", False),
    ("5.4 Redacción memoria (2° bimestre)", YELLOW, "$", "+", True),
    ("5.5 Documentación de uso e integración", GREEN, "$", "=", False),
    ("5.6 Informe de avances", GREEN, "$", "=", False),
    ("5.7 Preparación presentación final", YELLOW, "$", "=", False),
]

TaskItem = tuple[str, str | None, str | None, str | None, bool]


def _tc_borders(thick: bool = False) -> OxmlElement:
    borders = OxmlElement("w:tcBorders")
    sz = "18" if thick else "4"
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), sz)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    return borders


def _tc_properties(
    *,
    fill: str | None = None,
    grid_span: int = 1,
    thick: bool = False,
) -> OxmlElement:
    tc_pr = OxmlElement("w:tcPr")
    if grid_span > 1:
        gs = OxmlElement("w:gridSpan")
        gs.set(qn("w:val"), str(grid_span))
        tc_pr.append(gs)
    tc_pr.append(_tc_borders(thick))
    if fill:
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), fill)
        tc_pr.append(shd)
    tc_mar = OxmlElement("w:tcMar")
    for side in ("top", "left", "bottom", "right"):
        mar = OxmlElement(f"w:{side}")
        mar.set(qn("w:w"), "100")
        mar.set(qn("w:type"), "dxa")
        tc_mar.append(mar)
    tc_pr.append(tc_mar)
    v_align = OxmlElement("w:vAlign")
    v_align.set(qn("w:val"), "center")
    tc_pr.append(v_align)
    return tc_pr


def _text_paragraph(text: str, *, font_size: int = 10) -> OxmlElement:
    p = OxmlElement("w:p")
    p_pr = OxmlElement("w:pPr")
    jc = OxmlElement("w:jc")
    jc.set(qn("w:val"), "center")
    p_pr.append(jc)
    spacing = OxmlElement("w:spacing")
    spacing.set(qn("w:after"), "0")
    spacing.set(qn("w:line"), "240")
    spacing.set(qn("w:lineRule"), "auto")
    p_pr.append(spacing)
    p.append(p_pr)
    if text:
        r = OxmlElement("w:r")
        r_pr = OxmlElement("w:rPr")
        fonts = OxmlElement("w:rFonts")
        fonts.set(qn("w:ascii"), "Calibri")
        fonts.set(qn("w:hAnsi"), "Calibri")
        r_pr.append(fonts)
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), str(font_size * 2))
        r_pr.append(sz)
        r.append(r_pr)
        t = OxmlElement("w:t")
        t.set(qn("xml:space"), "preserve")
        t.text = text
        r.append(t)
        p.append(r)
    return p


def _make_cell(
    text: str = "",
    *,
    fill: str | None = None,
    grid_span: int = 1,
    thick: bool = False,
) -> OxmlElement:
    tc = OxmlElement("w:tc")
    tc.append(_tc_properties(fill=fill, grid_span=grid_span, thick=thick))
    tc.append(_text_paragraph(text))
    return tc


def _task_group_prefix(name: str) -> str:
    """Prefijo de grupo WBS: '1.1 Foo' -> '1'."""
    return name.split()[0].rsplit(".", 1)[0]


def _chunk_tasks(tasks: list[TaskItem], size: int = 4) -> list[list[TaskItem | None]]:
    """Agrupa por WBS (1.x, 2.x, ...) y completa cada fila hasta 4 celdas."""
    groups: list[list[TaskItem]] = []
    current: list[TaskItem] = []
    current_prefix: str | None = None
    for task in tasks:
        prefix = _task_group_prefix(task[0])
        if current_prefix is None or prefix == current_prefix:
            current.append(task)
            current_prefix = prefix
        else:
            groups.append(current)
            current = [task]
            current_prefix = prefix
    if current:
        groups.append(current)

    chunks: list[list[TaskItem | None]] = []
    for group in groups:
        for i in range(0, len(group), size):
            chunk: list[TaskItem | None] = list(group[i : i + size])
            while len(chunk) < size:
                chunk.append(None)
            chunks.append(chunk)
    return chunks


def build_task_grid_tbl(tasks: list[TaskItem] | None = None) -> OxmlElement:
    """Construye w:tbl con formato original: 8 columnas, 4 bloques por par de filas."""
    items = tasks if tasks is not None else TASKS
    tbl = OxmlElement("w:tbl")

    tbl_pr = OxmlElement("w:tblPr")
    tbl_w = OxmlElement("w:tblW")
    tbl_w.set(qn("w:w"), "5000")
    tbl_w.set(qn("w:type"), "pct")
    tbl_pr.append(tbl_w)
    tbl_borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        tbl_borders.append(el)
    tbl_pr.append(tbl_borders)
    tbl.append(tbl_pr)

    grid = OxmlElement("w:tblGrid")
    for _ in range(8):
        grid_col = OxmlElement("w:gridCol")
        grid_col.set(qn("w:w"), "1200")
        grid.append(grid_col)
    tbl.append(grid)

    for chunk in _chunk_tasks(items):
        title_row = OxmlElement("w:tr")
        symbol_row = OxmlElement("w:tr")
        for slot in chunk:
            if slot is None:
                title_row.append(_make_cell("", grid_span=2))
                symbol_row.append(_make_cell(""))
                symbol_row.append(_make_cell(""))
            else:
                name, color, cost, time, critical = slot
                title_row.append(
                    _make_cell(name, fill=color, grid_span=2, thick=critical)
                )
                symbol_row.append(_make_cell(cost or "", fill=color, thick=critical))
                symbol_row.append(_make_cell(time or "", fill=color, thick=critical))
        tbl.append(title_row)
        tbl.append(symbol_row)

    return tbl


def replace_task_table_after_anchor(doc, anchor_prefix: str = "IMPORTANTE: Indicar con borde grueso") -> None:
    """Elimina la tabla de tareas existente e inserta la grilla original."""
    from docx.table import Table

    anchor = None
    for p in doc.paragraphs:
        if p.text.strip().startswith(anchor_prefix):
            anchor = p
            break
    if anchor is None:
        raise ValueError(f"No se encontró ancla: {anchor_prefix}")

    task_table = None
    anchor_el = anchor._p
    for sibling in anchor_el.itersiblings():
        if sibling.tag == qn("w:tbl"):
            task_table = Table(sibling, anchor._parent)
            break

    new_tbl = build_task_grid_tbl()
    if task_table is not None:
        task_table._tbl.addnext(new_tbl)
        task_table._element.getparent().remove(task_table._element)
    else:
        anchor_el.addnext(new_tbl)


def style_task_table_for_docx(table) -> None:
    """Aplica ancho útil cuando la tabla ya está envuelta por python-docx."""
    table.autofit = False
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in paragraph.runs:
                    run.font.name = "Calibri"
                    run.font.size = Pt(10)
