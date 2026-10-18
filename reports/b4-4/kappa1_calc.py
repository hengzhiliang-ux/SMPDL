# -*- coding: utf-8 -*-
"""B4-4 kappa-1 computation: J-A (Kimi, cross-lineage) vs original adjudication (B4-2 v1.2 + B4-3 v1.0)
Pre-registered reading rule (K3, from work order B4-4 section 6, NOT modifiable post hoc):
  kappa >= 0.6        -> cross-lineage consistency holds
  0.4 <= kappa < 0.6  -> main-type retained, refinement downgraded (report divergent rounds honestly)
  kappa < 0.4         -> report honestly: same-lineage consistency NOT reproduced cross-lineage (valuable negative result, E4)

Coding disclosure (all decisions below are mechanical from the two adjudication texts):
  Three-tier layer: direct per-round three-tier verdicts (17 scored rounds; H46 control side excluded by protocol).
  Main-type layer A (classification): the ACTUAL main type each adjudicator assigned (4 categories: alpha/beta/gamma/alpha+meta).
     - R2 J-A wording "functional type is alpha/gamma rather than beta" coded as alpha (first-listed; both readings agree it is NOT beta).
     - R14 J-A "beta direction right, insufficient magnitude" coded as beta (directional classification).
  Main-type layer B (binary hit/miss): whether the adjudicator judged the REGISTERED main-type prediction as hit.
     Reported alongside A because B4-2/B4-3 headline kappas used hit-agreement construction; skew-paradox risk disclosed inline.
J-A batch-3 tally arithmetic slip (reported 6x full-hit, actual 7 incl B4-3-R2) does not affect per-round coding; registered as-is.
"""
from collections import Counter

ROUNDS = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12","R13","R14","B3-R1","B3-R2","B3-R3"]

# Three-tier verdicts (orig = B4-2 v1.2 / B4-3 v1.0; ja = J-A Kimi output)
ORIG_TIER = ["✅","❌","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","🟡","✅","🟡"]
JA_TIER   = ["🟡","❌","🟡","✅","✅","✅","✅","✅","🟡","❌","🟡","🟡","✅","❌","🟡","✅","🟡"]

# Actual main type assigned by each adjudicator (alpha/beta/gamma/meta where meta = alpha+meta-layer)
ORIG_MAIN = ["α","α","α","γ","β","β","meta","β","γ","β","β","β","β","β","β","α","α"]
JA_MAIN   = ["γ","α","α","γ","β","β","meta","β","γ","γ","β","β","β","β","α","α","α"]

# Registered predicted main type (from frozen files, operator column removed per forensics)
PRED_MAIN = ["α","β","α","γ","β","β","meta","β","γ","β","β","β","β","β","β","α","α"]

def cohen_kappa(a, b):
    assert len(a) == len(b)
    n = len(a)
    cats = sorted(set(a) | set(b))
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa, pb = Counter(a), Counter(b)
    pe = sum(pa[c] * pb[c] for c in cats) / (n * n)
    kap = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    return po, pe, kap

def main():
    print("=== B4-4 kappa-1: J-A (Kimi) vs original adjudication ===")
    print(f"n = {len(ROUNDS)} scored rounds (H46 quadratic-control side excluded by protocol)\n")

    # Layer 1: three-tier
    po, pe, k = cohen_kappa(ORIG_TIER, JA_TIER)
    print(f"[Three-tier layer]  raw agreement Po = {po:.3f} ({round(po*17)}/17), Pe = {pe:.3f}, kappa = {k:.3f}")
    tier_band = ">=0.6 consistency" if k >= 0.6 else ("[0.4,0.6) refinement downgrade" if k >= 0.4 else "<0.4 NOT reproduced cross-lineage")
    print(f"  K3 reading: {tier_band}\n")

    # Layer 2A: main-type classification
    po, pe, k = cohen_kappa(ORIG_MAIN, JA_MAIN)
    print(f"[Main-type classification] raw agreement Po = {po:.3f} ({round(po*17)}/17), Pe = {pe:.3f}, kappa = {k:.3f}")
    band = ">=0.6 consistency" if k >= 0.6 else ("[0.4,0.6) refinement downgrade" if k >= 0.4 else "<0.4 NOT reproduced")
    print(f"  K3 reading: {band}\n")

    # Layer 2B: binary hit/miss vs registered prediction (B4-2/B4-3 headline construction)
    orig_hit = ["✅" if o == p else "❌" for o, p in zip(ORIG_MAIN, PRED_MAIN)]
    ja_hit   = ["✅" if j == p else "❌" for j, p in zip(JA_MAIN, PRED_MAIN)]
    po, pe, k = cohen_kappa(orig_hit, ja_hit)
    print(f"[Main-hit binary]    raw agreement Po = {po:.3f} ({round(po*17)}/17), Pe = {pe:.3f}, kappa = {k:.3f}")
    print(f"  (skew warning: original hit rate {orig_hit.count('✅')}/17, J-A hit rate {ja_hit.count('✅')}/17 -> kappa paradox zone; raw agreement is the interpretable number here)\n")

    # Divergent rounds detail
    print("=== Divergent rounds ===")
    print("Three-tier divergences:")
    for r, o, j in zip(ROUNDS, ORIG_TIER, JA_TIER):
        if o != j:
            print(f"  {r}: orig {o} vs J-A {j}")
    print("Main-type divergences:")
    for r, o, j in zip(ROUNDS, ORIG_MAIN, JA_MAIN):
        if o != j:
            print(f"  {r}: orig {o} vs J-A {j}")
    print("\nJ-A miss rounds (main-layer):", [r for r, j, p in zip(ROUNDS, JA_MAIN, PRED_MAIN) if j != p])
    print("Orig miss rounds (main-layer):", [r for r, o, p in zip(ROUNDS, ORIG_MAIN, PRED_MAIN) if o != p])

if __name__ == "__main__":
    main()
