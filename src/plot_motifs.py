"""
Person 4: Generate the triad motif Z-score comparison chart.
Run from the project root folder:
    python src/plot_motifs.py
Requires pandas and matplotlib:
    pip install pandas matplotlib
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"

a = pd.read_csv(OUTPUT / "department_A_z_scores.csv")
b = pd.read_csv(OUTPUT / "department_B_z_scores.csv")

x = np.arange(1, 14)
width = 0.38

fig, ax = plt.subplots(figsize=(13, 7))
ax.bar(x - width / 2, a["Z-score"], width, label="Department A (ID 8)")
ax.bar(x + width / 2, b["Z-score"], width, label="Department B (ID 37)")
ax.axhline(2, linestyle="--", linewidth=1.5, label="Motif threshold (+2)")
ax.axhline(-2, linestyle="--", linewidth=1.5, label="Anti-motif threshold (−2)")
ax.axhline(0, linewidth=0.8)

ax.set_xlabel("Triad Class")
ax.set_ylabel("Z-score")
ax.set_title("Triad Motif Z-scores: Department 8 vs Department 37")
ax.set_xticks(x)
ax.set_xticklabels([str(i) for i in x])
ax.grid(axis="y", alpha=0.25)
ax.legend(ncol=2, loc="upper right")
fig.tight_layout()

destination = OUTPUT / "department_triad_motif_z_scores.png"
fig.savefig(destination, dpi=200, bbox_inches="tight")
print(f"Chart saved to: {destination}")
