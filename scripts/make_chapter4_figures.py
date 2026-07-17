"""Genera o mejora figuras del Capítulo 4 (demo logs y ciclo de vida de alerta).

Ejecutar desde la raíz del repositorio:

    python scripts/make_chapter4_figures.py
"""
from __future__ import annotations

from pathlib import Path

import shutil

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image


def make_demo_logs_figure(out_path: Path) -> None:
    """Recrea el extracto de logs con tipografía grande y proporción legible en PDF."""
    entries: list[tuple[str, str, str, str]] = [
        ("2026-06-18 18:42:34", "INFO", "Potential anomaly (1/2): error=0.7358 threshold=0.0025", "#e5e7eb"),
        (
            "2026-06-18 18:43:04",
            "WARN",
            "NEW ANOMALY: latency_p95=8.318 s recon_error=1.9231 confidence=298",
            "#fbbf24",
        ),
        ("2026-06-18 18:43:04", "INFO", "Alert sent via jsm: 8ee96543-...", "#e5e7eb"),
        ("2026-06-18 18:43:34", "INFO", "Anomaly ongoing (heartbeat, deduplicated)", "#e5e7eb"),
        ("2026-06-18 18:47:04", "INFO", "Anomaly ongoing (heartbeat, deduplicated)", "#e5e7eb"),
        (
            "2026-06-18 19:13:05",
            "WARN",
            "ESCALATION: active 30 min, error=21.94, alert sent via jsm",
            "#fbbf24",
        ),
        ("2026-06-18 21:02:22", "INFO", "RESOLVED: error below threshold, alert closed via jsm", "#e5e7eb"),
    ]

    line_count = len(entries)
    fig_h = 0.46 * line_count + 0.7
    fig, ax = plt.subplots(figsize=(12.8, fig_h))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panel = FancyBboxPatch(
        (0.005, 0.03),
        0.99,
        0.94,
        boxstyle="round,pad=0.01,rounding_size=0.02",
        linewidth=1.0,
        edgecolor="#475569",
        facecolor="#1f2937",
        zorder=0,
    )
    ax.add_patch(panel)

    mono = "DejaVu Sans Mono"
    fontsize = 13.0
    line_h = 0.88 / line_count
    y = 0.91

    for ts, level, message, color in entries:
        line = f"{ts}  {level:<4}  {message}"
        ax.text(
            0.025,
            y,
            line,
            ha="left",
            va="top",
            fontsize=fontsize,
            fontfamily=mono,
            color=color,
            zorder=1,
            clip_on=False,
        )
        y -= line_h

    fig.tight_layout(pad=0.15)
    fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def make_demo_logs_zoomed(out_path: Path, source_path: Path) -> None:
    """Recorta y amplía la captura de logs para mejorar legibilidad."""
    img = Image.open(source_path).convert("RGB")
    width, height = img.size

    # Recorte al bloque central de líneas de log (ajustado a la captura actual).
    left = int(width * 0.02)
    top = int(height * 0.08)
    right = int(width * 0.98)
    bottom = int(height * 0.92)
    cropped = img.crop((left, top, right, bottom))

    scale = 2.2
    zoomed = cropped.resize(
        (int(cropped.width * scale), int(cropped.height * scale)),
        Image.Resampling.LANCZOS,
    )
    zoomed.save(out_path, dpi=(300, 300))


def _draw_state_box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    label: str,
    facecolor: str,
    edgecolor: str,
    fontsize: float = 11.5,
) -> tuple[float, float, float, float]:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=1.2,
        edgecolor=edgecolor,
        facecolor=facecolor,
        zorder=2,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        label,
        ha="center",
        va="center",
        fontsize=fontsize,
        color="#0f172a",
        zorder=3,
        wrap=True,
    )
    return x, y, w, h


def _elbow_arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    lane_x: float,
    label: str | None = None,
    label_offset: tuple[float, float] = (-0.55, 0.0),
    fontsize: float = 9.5,
    color: str = "#475569",
) -> None:
    """Flecha en L por un carril vertical externo (no cruza el flujo central)."""
    x0, y0 = start
    x2, y2 = end
    ax.plot([x0, lane_x], [y0, y0], color=color, linewidth=1.2, zorder=1, solid_capstyle="round")
    ax.plot([lane_x, lane_x], [y0, y2], color=color, linewidth=1.2, zorder=1, solid_capstyle="round")
    ax.add_patch(
        FancyArrowPatch(
            (lane_x, y2),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.2,
            color=color,
            zorder=1,
        )
    )
    if label:
        ly = (y0 + y2) / 2
        ax.text(
            lane_x + label_offset[0],
            ly + label_offset[1],
            label,
            ha="center",
            va="center",
            fontsize=fontsize,
            color="#334155",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#e2e8f0", alpha=0.95),
            zorder=4,
        )


def _arrow(
    ax,
    p1: tuple[float, float],
    p2: tuple[float, float],
    label: str | None = None,
    label_offset: tuple[float, float] = (0.0, 0.0),
    rad: float = 0.0,
    fontsize: float = 9.5,
) -> None:
    style = f"arc3,rad={rad}" if rad else "arc3,rad=0"
    ax.add_patch(
        FancyArrowPatch(
            p1,
            p2,
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.2,
            color="#475569",
            connectionstyle=style,
            zorder=1,
        )
    )
    if label:
        lx = (p1[0] + p2[0]) / 2 + label_offset[0]
        ly = (p1[1] + p2[1]) / 2 + label_offset[1]
        ax.text(
            lx,
            ly,
            label,
            ha="center",
            va="center",
            fontsize=fontsize,
            color="#334155",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#e2e8f0", alpha=0.95),
            zorder=4,
        )


def make_ciclo_vida_alerta(out_path: Path) -> None:
    """Diagrama de estados del ciclo de vida de una alerta (flujo vertical legible en PDF)."""
    fig, ax = plt.subplots(figsize=(7.2, 7.4))
    ax.set_xlim(-0.25, 10.8)
    ax.set_ylim(0.4, 9.2)
    ax.axis("off")

    bw, bh = 2.85, 0.88
    box_fs = 12.5
    arrow_fs = 10.5
    cx = 3.55

    nominal = _draw_state_box(ax, cx, 7.55, bw, bh, "Operación\nnominal", "#dbeafe", "#2563eb", box_fs)
    potencial = _draw_state_box(ax, cx, 6.15, bw, bh, "Anomalía\npotencial", "#fef3c7", "#d97706", box_fs)
    nueva = _draw_state_box(
        ax, cx, 4.75, bw, bh, "Anomalía nueva\n(alerta de apertura)", "#ffedd5", "#ea580c", box_fs
    )
    curso = _draw_state_box(ax, cx, 3.35, bw, bh, "Anomalía\nen curso", "#fee2e2", "#dc2626", box_fs)
    escal = _draw_state_box(ax, 6.85, 3.35, bw, bh, "Escalamiento", "#fecaca", "#b91c1c", box_fs)
    resol = _draw_state_box(
        ax, cx, 1.55, bw, bh, "Resolución\n(notificación de cierre)", "#dcfce7", "#16a34a", box_fs
    )

    def center(box: tuple[float, float, float, float]) -> tuple[float, float]:
        x, y, w, h = box
        return x + w / 2, y + h / 2

    def right_mid(box: tuple[float, float, float, float]) -> tuple[float, float]:
        x, y, w, h = box
        return x + w, y + h / 2

    def left_mid(box: tuple[float, float, float, float]) -> tuple[float, float]:
        x, y, w, h = box
        return x, y + h / 2

    def bottom_mid(box: tuple[float, float, float, float]) -> tuple[float, float]:
        x, y, w, h = box
        return x + w / 2, y

    def top_mid(box: tuple[float, float, float, float]) -> tuple[float, float]:
        x, y, w, h = box
        return x + w / 2, y + h

    def left_lower(box: tuple[float, float, float, float], frac: float = 0.32) -> tuple[float, float]:
        x, y, w, h = box
        return x, y + h * frac

    # Flujo principal (vertical)
    _arrow(ax, bottom_mid(nominal), top_mid(potencial), "error > umbral\ny confianza ≥ mín.", (0.95, 0), fontsize=arrow_fs)
    _arrow(ax, bottom_mid(potencial), top_mid(nueva), "2 ciclos\nconsecutivos", (0.9, 0), fontsize=arrow_fs)
    _arrow(ax, bottom_mid(nueva), top_mid(curso), "misma\nanomalía", (0.85, 0), fontsize=arrow_fs)
    _arrow(ax, bottom_mid(curso), top_mid(resol), "error < umbral", (0.9, 0), fontsize=arrow_fs)

    # Retornos por carriles externos (sin atravesar el flujo central)
    lane_short = 1.55
    lane_long = 0.55

    _elbow_arrow(
        ax,
        left_mid(potencial),
        left_mid(nominal),
        lane_short,
        "ciclo nominal\no baja confianza",
        (-0.65, 0),
        fontsize=arrow_fs,
    )
    _elbow_arrow(
        ax,
        left_mid(resol),
        left_lower(nominal),
        lane_long,
        "vuelve a\nnominal",
        (-0.7, 0),
        fontsize=arrow_fs,
    )

    # Rama horizontal: en curso → escalamiento (etiqueta debajo de la flecha)
    _arrow(ax, right_mid(curso), left_mid(escal), "persiste\n> 30 min", (0, -0.48), fontsize=arrow_fs)

    # Heartbeat: bucle por encima de la flecha de escalamiento (carril derecho)
    cr = right_mid(curso)
    ct = top_mid(curso)
    lane_r = cr[0] + 0.55
    loop_y = ct[1] + 0.38
    y_out = cr[1] + 0.18
    ax.plot([cr[0], lane_r], [y_out, y_out], color="#475569", linewidth=1.2, zorder=1, solid_capstyle="round")
    ax.plot([lane_r, lane_r], [y_out, loop_y], color="#475569", linewidth=1.2, zorder=1, solid_capstyle="round")
    ax.add_patch(
        FancyArrowPatch(
            (lane_r, loop_y),
            (ct[0] + 0.22, ct[1]),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.2,
            color="#475569",
            zorder=1,
        )
    )
    ax.text(
        lane_r + 0.52,
        (y_out + loop_y) / 2 + 0.08,
        "heartbeat\n30 s",
        ha="center",
        va="center",
        fontsize=arrow_fs,
        color="#334155",
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#e2e8f0", alpha=0.95),
        zorder=4,
    )

    # Re-alerta: bucle sobre escalamiento (carril propio, sin solapar heartbeat)
    er = right_mid(escal)
    et = top_mid(escal)
    lane_esc = er[0] + 0.45
    loop_esc = et[1] + 0.38
    ax.plot([er[0], lane_esc], [er[1] + 0.18, er[1] + 0.18], color="#475569", linewidth=1.2, zorder=1, solid_capstyle="round")
    ax.plot([lane_esc, lane_esc], [er[1] + 0.18, loop_esc], color="#475569", linewidth=1.2, zorder=1, solid_capstyle="round")
    ax.add_patch(
        FancyArrowPatch(
            (lane_esc, loop_esc),
            (et[0] + 0.18, et[1]),
            arrowstyle="-|>",
            mutation_scale=12,
            linewidth=1.2,
            color="#475569",
            zorder=1,
        )
    )
    ax.text(
        lane_esc + 0.42,
        (er[1] + loop_esc) / 2 + 0.1,
        "re-alerta\n15 min",
        ha="center",
        va="center",
        fontsize=arrow_fs,
        color="#334155",
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#e2e8f0", alpha=0.95),
        zorder=4,
    )

    fig.tight_layout(pad=0.05)
    fig.savefig(out_path, dpi=300, bbox_inches="tight", pad_inches=0.03, facecolor="white")
    plt.close(fig)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    figures = root / "Figures"
    figures.mkdir(exist_ok=True)

    mpl.rcParams.update({"font.family": "serif", "font.size": 11})

    logs_src = figures / "demo_logs_source.png"
    logs_out = figures / "demo_logs.png"
    ciclo_out = figures / "ciclo_vida_alerta.png"

    if not logs_src.exists() and logs_out.exists():
        shutil.copy2(logs_out, logs_src)
        print(f"Backed up original to {logs_src.relative_to(root)}")

    make_demo_logs_figure(logs_out)
    print(f"Updated {logs_out.relative_to(root)}")

    make_ciclo_vida_alerta(ciclo_out)
    print(f"Saved {ciclo_out.relative_to(root)}")


if __name__ == "__main__":
    main()
