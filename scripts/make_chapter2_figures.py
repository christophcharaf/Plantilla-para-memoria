"""Genera figuras del Capítulo 2: distribución de métricas e infraestructura demo.

Los histogramas usan series sintéticas con estacionalidad diaria, alineadas
con la familia de métricas del mock service (no telemetría real de producción).

Ejecutar desde la raíz del repositorio:

    python scripts/make_chapter2_figures.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def _synthetic_metrics(n: int, rng: np.random.Generator) -> dict[str, np.ndarray]:
    """Generate plausible mock-service-like samples for histograms."""
    t = np.arange(n, dtype=float)
    hour = (t * 30 / 3600) % 24
    daily = 0.55 + 0.45 * np.sin(2 * np.pi * (hour - 6) / 24)
    weekend = (np.floor(t * 30 / 86400) % 7 >= 5).astype(float)
    daily = daily * (1.0 - 0.12 * weekend)

    request_rate = 125.0 * daily + rng.normal(0, 4.5, n)
    latency_p95 = 0.22 * daily + 0.215 + rng.normal(0, 0.012, n)
    memory_usage = (0.6e9 + 0.35e9 * daily + rng.normal(0, 2.5e7, n)).clip(4e8, 1.9e9)
    error_rate = (2.5 * daily * 0.02 + rng.exponential(0.004, n)).clip(0, None)
    cpu_usage = 0.125 * daily + rng.normal(0, 0.004, n)

    return {
        "request_rate": request_rate.clip(0, None),
        "latency_p95": latency_p95.clip(0, None),
        "memory_usage": memory_usage,
        "error_rate": error_rate,
        "cpu_usage": cpu_usage.clip(0, None),
    }


def make_dataset_distribution(out_path: Path) -> None:
    rng = np.random.default_rng(seed=11)
    n = 7 * 24 * 120  # 7 days @ 30 s
    data = _synthetic_metrics(n, rng)

    labels = {
        "request_rate": ("Tasa de peticiones (req/s)", "#1f77b4"),
        "latency_p95": ("Latencia p95 (s)", "#ff7f0e"),
        "memory_usage": ("Memoria residente (GB)", "#2ca02c"),
        "error_rate": ("Tasa de errores (err/s)", "#d62728"),
        "cpu_usage": ("Uso de CPU (núcleos)", "#9467bd"),
    }

    fig, axes = plt.subplots(2, 3, figsize=(9.2, 5.4))
    axes_flat = axes.ravel()

    for ax, (key, (title, color)) in zip(axes_flat, labels.items()):
        values = data[key]
        if key == "memory_usage":
            values = values / 1e9
        ax.hist(values, bins=40, color=color, alpha=0.78, edgecolor="white", linewidth=0.4)
        ax.set_title(title, fontsize=10)
        ax.set_ylabel("Frecuencia", fontsize=9)
        ax.set_xlabel("Valor", fontsize=9)
        ax.grid(True, alpha=0.25, linestyle="--", linewidth=0.5)

    axes_flat[-1].axis("off")
    fig.suptitle(
        "Distribución de métricas técnicas (datos sintéticos ilustrativos)",
        fontsize=11,
        y=1.02,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def make_infra_diagram(out_path: Path) -> None:
    """Topología demo: flujo horizontal claro con contenedor de red."""
    fig, ax = plt.subplots(figsize=(9.2, 4.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    container = FancyBboxPatch(
        (0.25, 0.35),
        9.5,
        4.25,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        linewidth=1.0,
        edgecolor="#94a3b8",
        facecolor="#f8fafc",
        linestyle=(0, (4, 3)),
        zorder=0,
    )
    ax.add_patch(container)
    ax.text(
        5.0,
        4.35,
        "Red puente interna (Docker Compose, perfil dev)",
        ha="center",
        va="center",
        fontsize=9.5,
        color="#64748b",
    )

    # x, y, width, height, label
    nodes = {
        "mock": (0.7, 2.85, 1.85, 0.95, "Servicio simulado\n(Flask)"),
        "prom": (3.95, 2.85, 2.1, 0.95, "Prometheus"),
        "graf": (7.45, 2.85, 1.85, 0.95, "Grafana"),
        "det": (3.95, 1.05, 2.1, 0.95, "Detector"),
        "ops": (7.45, 1.05, 1.85, 0.95, "Opsgenie"),
    }
    subtitles = {
        "mock": "Flask",
        "prom": "recolección",
        "graf": "visualización",
        "det": "inferencia",
        "ops": "alertas",
    }

    def draw_node(key: str) -> tuple[float, float, float, float]:
        x, y, w, h, title = nodes[key]
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=1.25,
            edgecolor="#334155",
            facecolor="#ffffff",
            zorder=2,
        )
        ax.add_patch(patch)
        ax.text(
            x + w / 2,
            y + h / 2 + 0.08,
            title,
            ha="center",
            va="center",
            fontsize=10,
            color="#0f172a",
            zorder=3,
        )
        ax.text(
            x + w / 2,
            y + h / 2 - 0.22,
            subtitles[key],
            ha="center",
            va="center",
            fontsize=8,
            color="#64748b",
            zorder=3,
        )
        return x, y, w, h

    boxes = {k: draw_node(k) for k in nodes}

    def connect(
        src: str,
        dst: str,
        src_anchor: str,
        dst_anchor: str,
        label: str | None = None,
        label_xy: tuple[float, float] | None = None,
    ) -> None:
        x1, y1, w1, h1 = boxes[src]
        x2, y2, w2, h2 = boxes[dst]
        anchors = {
            "left": lambda x, y, w, h: (x, y + h / 2),
            "right": lambda x, y, w, h: (x + w, y + h / 2),
            "top": lambda x, y, w, h: (x + w / 2, y + h),
            "bottom": lambda x, y, w, h: (x + w / 2, y),
        }
        p1 = anchors[src_anchor](x1, y1, w1, h1)
        p2 = anchors[dst_anchor](x2, y2, w2, h2)
        ax.annotate(
            "",
            xy=p2,
            xytext=p1,
            arrowprops=dict(
                arrowstyle="-|>",
                color="#475569",
                lw=1.3,
                shrinkA=2,
                shrinkB=2,
                connectionstyle="arc3,rad=0",
            ),
            zorder=1,
        )
        if label:
            lx, ly = label_xy if label_xy else ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            ax.text(
                lx,
                ly,
                label,
                ha="center",
                va="center",
                fontsize=8.5,
                color="#334155",
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="#e2e8f0", alpha=0.95),
                zorder=4,
            )

    connect("mock", "prom", "right", "left", "métricas", (2.75, 3.55))
    connect("prom", "graf", "right", "left")
    connect("prom", "det", "bottom", "top", "consultas PromQL", (5.65, 2.35))
    connect("det", "ops", "right", "left", "alertas", (6.75, 1.55))

    fig.tight_layout(pad=0.15)
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

    dist_path = out_dir / "dataset_distribution.png"
    infra_path = out_dir / "infra_demo.png"

    make_dataset_distribution(dist_path)
    make_infra_diagram(infra_path)

    print(f"Saved {dist_path.relative_to(out_dir.parent)}")
    print(f"Saved {infra_path.relative_to(out_dir.parent)}")


if __name__ == "__main__":
    main()
