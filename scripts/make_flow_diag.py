"""Genera Figures/flow_diag.png — flujo interno del detector (Cap. 3).

Ejecutar desde la raíz del repositorio:

    python scripts/make_flow_diag.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon


def _box(
    ax,
    x: float,
    y: float,
    w: float,
    h: float,
    label: str,
    *,
    facecolor: str = "#ffffff",
    edgecolor: str = "#0f766e",
    fontsize: float = 11.5,
    shape: str = "rect",
) -> tuple[float, float, float, float]:
    if shape == "oval":
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.45",
            linewidth=1.2,
            edgecolor=edgecolor,
            facecolor=facecolor,
            zorder=2,
        )
    elif shape == "doc":
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
        ax.plot([x + 0.08, x + 0.08], [y, y + h], color=edgecolor, linewidth=1.0, zorder=3)
    else:
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
        zorder=4,
        wrap=True,
    )
    return x, y, w, h


def _arrow(ax, p1, p2, label: str | None = None, label_offset=(0, 0), fontsize=10.0) -> None:
    ax.add_patch(
        FancyArrowPatch(
            p1,
            p2,
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=1.2,
            color="#475569",
            zorder=1,
        )
    )
    if label:
        ax.text(
            (p1[0] + p2[0]) / 2 + label_offset[0],
            (p1[1] + p2[1]) / 2 + label_offset[1],
            label,
            ha="center",
            va="center",
            fontsize=fontsize,
            color="#334155",
            zorder=5,
        )


def _diamond(ax, cx: float, cy: float, w: float, h: float, label: str, fontsize=11.5) -> None:
    pts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
    ax.add_patch(Polygon(pts, closed=True, facecolor="#ecfeff", edgecolor="#0e7490", linewidth=1.2, zorder=2))
    ax.text(cx, cy, label, ha="center", va="center", fontsize=fontsize, color="#0f172a", zorder=4)


def make_flow_diag(out_path: Path) -> None:
    title_fs = 11.5
    sub_fs = 10.5
    label_fs = 10.0

    fig, ax = plt.subplots(figsize=(7.8, 8.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    prom = _box(ax, 3.55, 9.05, 2.9, 0.72, "Prometheus", facecolor="#ccfbf1", edgecolor="#0f766e", fontsize=title_fs, shape="oval")
    df = _box(ax, 3.35, 7.85, 3.3, 0.72, "Dataframe con\nMétricas", facecolor="#f0fdfa", edgecolor="#0f766e", fontsize=title_fs, shape="doc")
    pre = _box(
        ax,
        2.15,
        6.55,
        5.7,
        0.82,
        "Preprocesamiento de datos\ny feature engineering",
        facecolor="#ffffff",
        edgecolor="#0f766e",
        fontsize=title_fs,
    )

    ae_box = FancyBboxPatch(
        (1.35, 2.55),
        7.3,
        3.55,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        linewidth=1.2,
        edgecolor="#0891b2",
        facecolor="#ecfeff",
        zorder=0,
    )
    ax.add_patch(ae_box)
    ax.text(5.0, 5.85, "LSTM Autoencoder", ha="center", fontsize=12.5, color="#0e7490", fontweight="bold")

    enc = _box(ax, 1.75, 4.55, 2.35, 0.78, "Encoder\nLSTM", facecolor="#ffffff", edgecolor="#0891b2", fontsize=title_fs)
    dec = _box(ax, 4.45, 4.55, 2.35, 0.78, "Decoder\nLSTM", facecolor="#ffffff", edgecolor="#0891b2", fontsize=title_fs)
    recon = _box(ax, 4.25, 3.35, 2.75, 0.72, "Reconstrucción\nde métricas", facecolor="#ffffff", edgecolor="#0891b2", fontsize=title_fs)
    cmp = _box(ax, 4.05, 2.75, 3.15, 0.62, "Comparación\ncon umbral", facecolor="#ffffff", edgecolor="#0891b2", fontsize=title_fs)

    _diamond(ax, 5.0, 1.55, 1.55, 0.95, "Anomalía", fontsize=title_fs)
    grafana = _box(ax, 1.55, 0.35, 2.55, 0.72, "Enlace a\nGrafana", facecolor="#f0fdfa", edgecolor="#0f766e", fontsize=title_fs)
    ops = _box(ax, 6.05, 0.35, 2.55, 0.72, "Alerta\nOpsgenie", facecolor="#f0fdfa", edgecolor="#0f766e", fontsize=title_fs)

    def bottom(b):
        return (b[0] + b[2] / 2, b[1])

    def top(b):
        return (b[0] + b[2] / 2, b[1] + b[3])

    def right_mid(b):
        return (b[0] + b[2], b[1] + b[3] / 2)

    def left_mid(b):
        return (b[0], b[1] + b[3] / 2)

    _arrow(ax, bottom(prom), top(df), "API", (0.35, 0), fontsize=label_fs)
    _arrow(ax, bottom(df), top(pre))
    _arrow(ax, bottom(pre), (5.0, 6.1))
    _arrow(ax, right_mid(enc), left_mid(dec))
    _arrow(ax, bottom(dec), top(recon))
    _arrow(ax, bottom(recon), top(cmp))
    _arrow(ax, bottom(cmp), (5.0, 2.02))

    _arrow(ax, (4.22, 1.55), left_mid(grafana), "Sí", (-0.15, 0.18), fontsize=label_fs)
    _arrow(ax, (5.78, 1.55), left_mid(ops), "Sí", (0.15, 0.18), fontsize=label_fs)
    ax.annotate(
        "",
        xy=(3.55, 9.41),
        xytext=(3.35, 1.55),
        arrowprops=dict(arrowstyle="-|>", color="#475569", lw=1.2, connectionstyle="arc3,rad=-0.55"),
        zorder=1,
    )
    ax.text(2.05, 5.35, "No", fontsize=label_fs, color="#334155", rotation=90, va="center")

    fig.tight_layout(pad=0.05)
    fig.savefig(out_path, dpi=280, bbox_inches="tight", facecolor="white", pad_inches=0.04)
    plt.close(fig)


def main() -> None:
    out_dir = Path(__file__).resolve().parents[1] / "Figures"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "flow_diag.png"

    mpl.rcParams.update({"font.family": "serif", "font.size": 11})
    make_flow_diag(out_path)
    print(f"Saved {out_path.relative_to(out_path.parents[1])}")


if __name__ == "__main__":
    main()
