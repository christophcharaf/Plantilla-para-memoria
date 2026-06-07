"""Genera la figura del Capítulo 3: ventanas deslizantes en la detección.

Ilustra cómo la serie temporal multivariada se segmenta en secuencias
solapadas de tamaño fijo (window_size=20 timesteps ≈ 10 min con muestreo
de 30 s, stride=1) que alimentan al autoencoder LSTM. El esquema es
ilustrativo y refleja la configuración real de ``config/windowing.yaml``.

Ejecutar desde la raíz del repositorio:

    python scripts/make_sliding_window_figure.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


WINDOW_SIZE = 20
STRIDE = 1
SAMPLING_SECONDS = 30


def _series(n: int, rng: np.random.Generator) -> np.ndarray:
    """Serie sintética suave con estacionalidad, sólo para ilustrar."""
    t = np.arange(n, dtype=float)
    daily = 0.55 + 0.45 * np.sin(2 * np.pi * (t - 6) / n)
    return (daily + rng.normal(0, 0.03, n)).clip(0, None)


def make_sliding_window(out_path: Path) -> None:
    rng = np.random.default_rng(seed=7)
    n_points = 28  # timesteps mostrados en el eje
    series = _series(n_points, rng)

    fig, (ax_top, ax_bot) = plt.subplots(
        2,
        1,
        figsize=(9.4, 5.6),
        gridspec_kw={"height_ratios": [2.0, 1.15], "hspace": 0.42},
    )

    # ------------------------------------------------------------------
    # Panel superior: serie temporal con ventanas solapadas resaltadas
    # ------------------------------------------------------------------
    x = np.arange(n_points)
    ax_top.plot(x, series, color="#1f77b4", lw=1.6, zorder=3)
    ax_top.scatter(x, series, s=18, color="#1f77b4", zorder=4)

    win_len = 12  # tamaño dibujado (compacto); rotulado como window_size real
    windows = [(0, "#2ca02c"), (1, "#ff7f0e"), (2, "#9467bd")]
    y0, y1 = -0.12, 1.18
    label_y = {0: 1.36, 1: 1.54, 2: 1.72}  # escalonado para evitar solapamiento

    for offset, color in windows:
        start = offset
        rect = FancyBboxPatch(
            (start - 0.42, y0),
            win_len - 0.16,
            y1 - y0,
            boxstyle="round,pad=0.0,rounding_size=0.08",
            linewidth=1.5,
            edgecolor=color,
            facecolor=color,
            alpha=0.12,
            zorder=2,
        )
        ax_top.add_patch(rect)
        ax_top.text(
            start - 0.42,
            label_y[offset],
            f"Ventana {offset + 1}",
            ha="left",
            va="center",
            fontsize=8.5,
            color=color,
            fontweight="bold",
            zorder=5,
            clip_on=False,
        )

    # Flecha que indica el desplazamiento (stride)
    ax_top.annotate(
        "",
        xy=(1.0, y0 - 0.12),
        xytext=(0.0, y0 - 0.12),
        arrowprops=dict(arrowstyle="-|>", color="#334155", lw=1.4),
        annotation_clip=False,
    )
    ax_top.text(
        0.5,
        y0 - 0.28,
        f"stride = {STRIDE}",
        ha="center",
        va="top",
        fontsize=8.5,
        color="#334155",
        clip_on=False,
    )

    # Doble flecha que indica el tamaño de ventana
    minutes = WINDOW_SIZE * SAMPLING_SECONDS // 60
    ax_top.annotate(
        "",
        xy=(win_len - 1 - 0.42, 2.06),
        xytext=(-0.42, 2.06),
        arrowprops=dict(arrowstyle="<|-|>", color="#0f172a", lw=1.4),
        annotation_clip=False,
    )
    ax_top.text(
        (win_len - 1) / 2 - 0.42,
        2.18,
        f"window_size = {WINDOW_SIZE} timesteps  (≈ {minutes} min @ {SAMPLING_SECONDS}s)",
        ha="center",
        va="bottom",
        fontsize=9,
        color="#0f172a",
        clip_on=False,
    )

    ax_top.set_xlim(-1.2, n_points - 0.5)
    ax_top.set_ylim(y0 - 0.5, 2.4)
    ax_top.set_xlabel("Tiempo (timesteps, muestreo cada 30 s)", fontsize=9)
    ax_top.set_ylabel("Métrica\n(normalizada)", fontsize=9)
    ax_top.set_yticks([])
    ax_top.grid(True, axis="x", alpha=0.2, linestyle="--", linewidth=0.5)
    ax_top.set_title(
        "Segmentación en ventanas deslizantes solapadas",
        fontsize=11,
        pad=26,
    )

    # ------------------------------------------------------------------
    # Panel inferior: una ventana -> autoencoder -> error de reconstrucción
    # ------------------------------------------------------------------
    ax_bot.set_xlim(0, 10)
    ax_bot.set_ylim(0, 2)
    ax_bot.axis("off")

    def box(cx: float, w: float, label: str, sub: str, color: str) -> tuple[float, float]:
        h = 0.95
        patch = FancyBboxPatch(
            (cx - w / 2, 0.5),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=1.3,
            edgecolor="#334155",
            facecolor=color,
            zorder=2,
        )
        ax_bot.add_patch(patch)
        ax_bot.text(cx, 0.5 + h / 2 + 0.1, label, ha="center", va="center",
                    fontsize=9.5, color="#0f172a", zorder=3)
        ax_bot.text(cx, 0.5 + h / 2 - 0.2, sub, ha="center", va="center",
                    fontsize=8, color="#475569", zorder=3)
        return cx - w / 2, cx + w / 2

    _, r1 = box(1.7, 2.6, "Ventana", f"{WINDOW_SIZE} timesteps × 5+ features", "#e8f1fb")
    l2, r2 = box(5.0, 2.7, "Autoencoder LSTM", "encoder → cuello → decoder", "#eef7ee")
    l3, _ = box(8.4, 2.7, "Error de reconstrucción", "compara con umbral (p95)", "#fdeee8")

    for xa, xb in ((r1, l2), (r2, l3)):
        ax_bot.add_patch(
            FancyArrowPatch(
                (xa + 0.05, 0.975),
                (xb - 0.05, 0.975),
                arrowstyle="-|>",
                mutation_scale=14,
                color="#475569",
                lw=1.4,
                zorder=1,
            )
        )

    fig.savefig(out_path, dpi=240, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main() -> None:
    out_dir = Path(__file__).resolve().parents[1] / "Figures"
    out_dir.mkdir(exist_ok=True)

    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )

    out_path = out_dir / "sliding_window.png"
    make_sliding_window(out_path)
    print(f"Saved {out_path.relative_to(out_dir.parent)}")


if __name__ == "__main__":
    main()
