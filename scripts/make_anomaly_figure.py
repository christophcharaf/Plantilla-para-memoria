"""Genera Figures/anomaly_example.png para el Capítulo 1 de la memoria.

Muestra una métrica sintética con estacionalidad diaria, una banda
de "régimen nominal esperado" y una ventana donde se inyectó una
anomalía. Se utiliza únicamente con fines ilustrativos.

Ejecutar desde la raíz del repositorio:

    python scripts/make_anomaly_figure.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    out_dir = Path(__file__).resolve().parents[1] / "Figures"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "anomaly_example.png"

    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titleweight": "regular",
        }
    )

    rng = np.random.default_rng(seed=7)
    t = np.linspace(0, 24, 480)

    seasonal = 50.0 + 15.0 * np.sin(2 * np.pi * t / 24 - np.pi / 2) + 6.0 * np.sin(
        2 * np.pi * t / 6
    )
    noise = rng.normal(0.0, 1.8, size=t.size)
    metric = seasonal + noise

    band_half_width = 6.5
    upper_band = seasonal + band_half_width
    lower_band = seasonal - band_half_width

    a_start = 280
    a_end = 360
    bump = 28.0 * np.exp(-0.5 * ((np.arange(a_end - a_start) - 25) / 18.0) ** 2)
    metric[a_start:a_end] = (
        seasonal[a_start:a_end] + bump + rng.normal(0.0, 2.5, size=a_end - a_start)
    )

    fig, ax = plt.subplots(figsize=(8.4, 3.6))

    ax.fill_between(
        t,
        lower_band,
        upper_band,
        color="#2ca02c",
        alpha=0.18,
        linewidth=0,
        label="Régimen nominal esperado",
    )
    ax.plot(t, seasonal, color="#2ca02c", linewidth=0.8, alpha=0.5)
    ax.plot(t, metric, color="#1f77b4", linewidth=1.2, label="Métrica observada")
    ax.plot(
        t[a_start:a_end],
        metric[a_start:a_end],
        color="#d62728",
        linewidth=1.6,
        label="Anomalía",
    )

    ax.axvspan(t[a_start], t[a_end - 1], color="#d62728", alpha=0.10, linewidth=0)

    peak_idx = a_start + int(np.argmax(metric[a_start:a_end]))
    ax.annotate(
        "Desvío del\ncomportamiento\nhabitual",
        xy=(t[peak_idx], metric[peak_idx]),
        xytext=(t[peak_idx] + 1.2, metric[peak_idx] + 5),
        fontsize=9,
        ha="left",
        arrowprops=dict(arrowstyle="->", color="#444", lw=0.8),
    )

    ax.set_xlabel("Tiempo (horas)")
    ax.set_ylabel("Métrica (unidades arbitrarias)")
    ax.set_xlim(0, 24)
    ax.set_xticks([0, 4, 8, 12, 16, 20, 24])
    ax.legend(loc="upper left", framealpha=0.9, fontsize=9, ncol=1)
    ax.grid(True, alpha=0.3, linestyle="--", linewidth=0.6)

    fig.tight_layout()
    fig.savefig(out_path, dpi=220, bbox_inches="tight")
    print(f"Saved {out_path.relative_to(out_path.parents[1])}")


if __name__ == "__main__":
    main()
