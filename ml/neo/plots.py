"""Chart helpers with one consistent, colour-blind-safe style.

Rules followed (validated palette, light surface):
- one colour for one series; a legend only when there are two or more series;
- categorical colours are taken in a fixed order, never cycled;
- thin bars, a 2-pixel gap in the surface colour between touching segments;
- text is always dark ink, never the series colour; grid and axes stay quiet.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# Same input, same SVG file: fixed ids instead of random ones (see save()).
mpl.rcParams["svg.hashsalt"] = "neo-helper"

SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e6e5e1"
# Fixed categorical order: blue, orange, aqua, yellow, magenta, green, violet, red.
SERIES = ("#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948")


def new_figure(width: float = 7.0, height: float = 3.6) -> tuple[Figure, Axes]:
    """A figure with the common style applied."""
    fig, ax = plt.subplots(figsize=(width, height), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=TEXT_SECONDARY, length=0, labelsize=9)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    return fig, ax


def _title(ax: Axes, title: str, subtitle: str | None) -> None:
    ax.set_title(title, loc="left", color=TEXT, fontsize=11, fontweight="bold", pad=22)
    if subtitle:
        ax.text(0, 1.03, subtitle, transform=ax.transAxes, color=TEXT_SECONDARY, fontsize=9)


def bar_counts(
    counts: pd.Series,
    title: str,
    subtitle: str | None = None,
    show_share: bool = True,
) -> Figure:
    """Horizontal bars for one series of counts, largest on top, each with its value."""
    counts = counts.sort_values()
    fig, ax = new_figure(height=0.42 * len(counts) + 1.3)
    bars = ax.barh(counts.index.astype(str), counts.to_numpy(), height=0.55, color=SERIES[0])
    total = counts.sum()
    for bar, value in zip(bars, counts.to_numpy(), strict=True):
        label = f"{value:,}".replace(",", " ")
        if show_share:
            label += f"  ({value / total:.1%})"
        ax.text(
            bar.get_width(),
            bar.get_y() + bar.get_height() / 2,
            "  " + label,
            va="center",
            color=TEXT,
            fontsize=9,
        )
    ax.set_xlim(0, counts.max() * 1.22)
    ax.tick_params(axis="y", labelcolor=TEXT, labelsize=10)
    _title(ax, title, subtitle)
    fig.tight_layout()
    return fig


def bar_shares(
    shares: pd.Series,
    counts: pd.Series,
    title: str,
    subtitle: str | None = None,
) -> Figure:
    """Horizontal bars for one series of shares (0 to 1), labelled "12.3%  (45 of 366)".

    ``counts`` gives the size of each group, in the same order as ``shares``.
    """
    order = shares.sort_values().index
    shares, counts = shares.loc[order], counts.loc[order]
    fig, ax = new_figure(height=0.42 * len(shares) + 1.3)
    bars = ax.barh(shares.index.astype(str), shares.to_numpy(), height=0.55, color=SERIES[0])
    for bar, share, size in zip(bars, shares.to_numpy(), counts.to_numpy(), strict=True):
        ax.text(
            bar.get_width(),
            bar.get_y() + bar.get_height() / 2,
            f"  {share:.1%}  ({round(share * size)} of {size})",
            va="center",
            color=TEXT,
            fontsize=9,
        )
    ax.set_xlim(0, max(shares.max() * 1.45, 0.05))
    ax.xaxis.set_major_formatter(lambda x, _: f"{x:.0%}")
    ax.tick_params(axis="y", labelcolor=TEXT, labelsize=10)
    _title(ax, title, subtitle)
    fig.tight_layout()
    return fig


def stacked_share(
    table: pd.DataFrame,
    title: str,
    subtitle: str | None = None,
    min_label: float = 0.07,
) -> Figure:
    """100% stacked horizontal bars: one row per index value, one segment per column.

    ``table`` holds counts; rows are converted to shares. Segments wide enough
    carry their percentage; the legend names the series.
    """
    if table.shape[1] > len(SERIES):
        raise ValueError(f"At most {len(SERIES)} series: fold the smallest into 'other'")
    share = table.div(table.sum(axis=1), axis=0).iloc[::-1]
    fig, ax = new_figure(height=0.42 * len(share) + 1.9)
    left = pd.Series(0.0, index=share.index)
    for position, column in enumerate(share.columns):
        values = share[column]
        ax.barh(
            share.index.astype(str),
            values,
            left=left,
            height=0.55,
            color=SERIES[position],
            edgecolor=SURFACE,  # the gap between touching segments
            linewidth=2,
            label=str(column),
        )
        for row, value in values.items():
            if value >= min_label:
                ax.text(
                    left[row] + value / 2,
                    str(row),
                    f"{value:.0%}",
                    ha="center",
                    va="center",
                    color=TEXT if position in (2, 3, 4) else "white",
                    fontsize=8.5,
                )
        left = left + values
    ax.set_xlim(0, 1)
    ax.xaxis.set_major_formatter(lambda x, _: f"{x:.0%}")
    ax.tick_params(axis="y", labelcolor=TEXT, labelsize=10)
    ax.legend(
        loc="upper left",
        bbox_to_anchor=(0, -0.12),
        ncol=len(share.columns),
        frameon=False,
        fontsize=9,
        labelcolor=TEXT_SECONDARY,
        handlelength=1,
        handleheight=1,
        columnspacing=1.4,
    )
    _title(ax, title, subtitle)
    fig.tight_layout()
    return fig


def save(fig: Figure, folder: Path, name: str) -> list[Path]:
    """Save ``fig`` as SVG (source) and PNG (2x) in ``folder``."""
    folder.mkdir(parents=True, exist_ok=True)
    written = []
    # No creation date in the files, so re-running a notebook does not change them.
    for suffix, options in ((".svg", {"metadata": {"Date": None}}), (".png", {"dpi": 200})):
        path = folder / f"{name}{suffix}"
        fig.savefig(path, facecolor=SURFACE, bbox_inches="tight", **options)
        written.append(path)
    return written
