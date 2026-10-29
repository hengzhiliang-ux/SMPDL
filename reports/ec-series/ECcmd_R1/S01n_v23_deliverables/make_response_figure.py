from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

root = Path(__file__).resolve().parent
df = pd.read_csv(root / "spectral_response_k1_40.csv")
sample = df[(df.k >= 5) & (df.k <= 40)]
rho = sample.delta_k.corr(sample.d_k)

fig, ax = plt.subplots(figsize=(8.2, 5.2), dpi=180)
ax.scatter(sample.d_k, sample.delta_k, s=34, color="#2457A6", edgecolor="white", linewidth=0.5)
for k in (5, 10, 20, 30, 40):
    row = sample[sample.k == k].iloc[0]
    ax.annotate(f"k={k}", (row.d_k, row.delta_k), xytext=(6, 5), textcoords="offset points", fontsize=8)
ax.set_xlabel(r"Zero gap $d_k=\gamma_k-2\mu_k$")
ax.set_ylabel(r"First-order response $\delta_k=E_k^{(1)}/(4\mu_k)$")
ax.set_title(f"Spectral response, k=5..40\nPearson correlation = {rho:.10f}")
ax.grid(alpha=0.22)
fig.tight_layout()
fig.savefig(root / "spectral_response_scatter.png", bbox_inches="tight")
print(f"rho={rho:.15f}")
print(f"lambda_negative_rho={-rho:.15f}")
print(f"lambda_negative_same_sign={int(((sample.d_k) * (-sample.delta_k) > 0).sum())}/{len(sample)}")
