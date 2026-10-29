"""S01 v2.3: first-order spectral response of the Bessel mechanism.

Primary convention: B=-d^2/dt^2+a^2 exp(2*kappa*t) on L^2(0,infty),
Dirichlet at t=0, a=4/pi, kappa=2, z0=a/kappa=2/pi.
All Bessel evaluations and normalization derivatives use mpmath.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

OUT = Path(__file__).resolve().parent
KAPPA = 2.0
A = 4.0 / math.pi
Z0 = A / KAPPA
NSTATES = 40
K_MIN = 5
PRIMARY_SIGMA = 0.25
PRIMARY_R = 2000


def bessel_value(mu: float, x: float) -> float:
    # For real x>0 and real mu, K_{i mu}(x) is real; discard roundoff imag part.
    return float(mp.re(mp.besselk(1j * mp.mpf(mu), mp.mpf(x))))


def find_mu_roots(count: int) -> list[float]:
    """Ordered positive roots of K_{i mu}(z0)=0 by sign bracketing."""
    roots: list[float] = []
    step = 0.025
    left = 0.05
    f_left = bessel_value(left, Z0)
    right = left + step
    while len(roots) < count:
        f_right = bessel_value(right, Z0)
        if f_left == 0.0:
            root = left
        elif f_left * f_right < 0.0:
            root = float(
                mp.findroot(
                    lambda u: mp.re(mp.besselk(1j * u, mp.mpf(Z0))),
                    (mp.mpf(left), mp.mpf(right)),
                    solver="bisect",
                    tol=mp.mpf("1e-45"),
                )
            )
        else:
            root = None
        if root is not None:
            if not roots or abs(root - roots[-1]) > 1e-8:
                roots.append(root)
                print(f"mu[{len(roots)}] = {root:.15f}", flush=True)
        left, f_left = right, f_right
        right += step
        if right > 200:
            raise RuntimeError("Root search exceeded mu=200")
    return roots


def normalization(mu: float) -> float:
    """N^2 = integral_0^infty K_{i mu}(z0 exp(kappa*t))^2 dt.

    Differentiate the eigenvalue equation in the energy and use the
    Dirichlet Wronskian identity. For kappa=2 this is
    N^2 = -z0 K_x(z0) K_mu(z0)/(2*kappa*mu).
    """
    m = mp.mpf(mu)
    z = mp.mpf(Z0)
    kx = mp.diff(lambda x: mp.besselk(1j * m, x), z)
    kmu = mp.diff(lambda u: mp.besselk(1j * u, z), m)
    n2 = mp.re(-z * kx * kmu / (2 * mp.mpf(KAPPA) * m))
    if n2 <= 0:
        raise RuntimeError(f"Nonpositive norm at mu={mu}: {n2}")
    return float(mp.sqrt(n2))


def prime_power_weights(radius: int) -> tuple[np.ndarray, np.ndarray]:
    """Return n and Lambda(n)/sqrt(n) for 2<=n<=radius."""
    spf = list(range(radius + 1))
    for p in range(2, int(radius**0.5) + 1):
        if spf[p] == p:
            for n in range(p * p, radius + 1, p):
                if spf[n] == n:
                    spf[n] = p
    ns: list[int] = []
    weights: list[float] = []
    for n in range(2, radius + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:  # n is a power of p
            ns.append(n)
            weights.append(math.log(p) / math.sqrt(n))
    return np.asarray(ns, dtype=int), np.asarray(weights, dtype=float)


def integrate_unnormalized(mu: float, t_eval: np.ndarray) -> np.ndarray:
    """Decaying eigenfunction branch obtained by stable inward integration."""
    def rhs(t: float, y: np.ndarray) -> tuple[float, float]:
        return y[1], (A * A * math.exp(2.0 * KAPPA * t) - KAPPA * KAPPA * mu * mu) * y[0]

    right = float(t_eval[-1])
    decay_rate = math.sqrt(A * A * math.exp(2.0 * KAPPA * right) - KAPPA * KAPPA * mu * mu)
    # WKB amplitude scaling prevents overflow during inward integration.
    amplitude = math.exp(-Z0 * math.exp(KAPPA * right))
    reversed_grid = t_eval[::-1]
    solution = solve_ivp(
        rhs,
        (right, 0.0),
        (amplitude, -decay_rate * amplitude),
        t_eval=reversed_grid,
        method="DOP853",
        rtol=2e-12,
        atol=1e-300,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution.y[0, ::-1]


def make_density_grid(mus: list[float], h: float = 0.002) -> tuple[np.ndarray, np.ndarray]:
    """Normalized |psi_k(t)|^2 on a common trapezoidal grid."""
    t_max = max(0.5 * math.log(mu / Z0) for mu in mus) + 2.0
    grid = np.arange(0.0, t_max + 0.5 * h, h)
    densities = np.zeros((len(mus), len(grid)), dtype=float)
    for i, mu in enumerate(mus):
        turning = 0.5 * math.log(mu / Z0)
        # Far beyond the turning point the decaying branch is negligible.
        cutoff = turning + 1.2
        active = grid <= cutoff
        values = integrate_unnormalized(mu, grid[active])
        raw_density = values * values
        raw_mass = np.trapezoid(raw_density, grid[active])
        densities[i, active] = raw_density / raw_mass
        mass = np.trapezoid(densities[i], grid)
        tail_mass = np.trapezoid(densities[i, grid > turning + 1.2], grid[grid > turning + 1.2])
        print(
            f"density[{i+1}]: grid_mass={mass:.12f}, "
            f"tail>{turning+1.2:.3f}={tail_mass:.3e}",
            flush=True,
        )
        if abs(mass - 1.0) > 2e-7:
            raise RuntimeError(f"Grid normalization failed at k={i+1}: {mass}")
    return grid, densities


def responses(
    mus: list[float],
    grid: np.ndarray,
    densities: np.ndarray,
    sigma: float,
    radius: int,
) -> tuple[np.ndarray, np.ndarray]:
    ns, weights = prime_power_weights(radius)
    logs = np.log(ns.astype(float))
    e1 = np.zeros(len(mus), dtype=float)
    # Chunk over n to keep memory bounded for sensitivity runs.
    for start in range(0, len(ns), 128):
        stop = min(start + 128, len(ns))
        chi = np.exp(-0.5 * ((grid[None, :] - logs[start:stop, None]) / sigma) ** 2)
        chi /= math.sqrt(2.0 * math.pi) * sigma
        sampled = densities @ chi.T * (grid[1] - grid[0])
        e1 += sampled @ weights[start:stop]
    delta = e1 / (2.0 * KAPPA * np.asarray(mus))
    return e1, delta


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def main() -> None:
    mp.mp.dps = 60
    mus = find_mu_roots(NSTATES)
    gammas = [float(mp.im(mp.zetazero(k))) for k in range(1, NSTATES + 1)]
    grid, densities = make_density_grid(mus)

    # Cross-check Wronskian normalization against ODE quadrature.
    norm_checks = []
    for k in (1, 5, 20, 40):
        mu_value = mus[k - 1]
        turning = 0.5 * math.log(mu_value / Z0)
        check_grid = np.arange(0.0, turning + 1.2, 0.001)
        values = integrate_unnormalized(mu_value, check_grid)
        raw_mass = np.trapezoid(values * values, check_grid)
        k_at_turning = bessel_value(mu_value, mu_value)
        y_at_turning = float(np.interp(turning, check_grid, values))
        scale = k_at_turning / y_at_turning  # K = scale * y
        n2_quad = raw_mass * scale * scale
        n2_formula = normalization(mu_value) ** 2
        norm_checks.append(
            {
                "k": k,
                "ode_quadrature": n2_quad,
                "wronskian": n2_formula,
                "relative_error": abs(n2_quad / n2_formula - 1),
            }
        )

    e1, delta = responses(mus, grid, densities, PRIMARY_SIGMA, PRIMARY_R)
    d = np.asarray(gammas) - KAPPA * np.asarray(mus)
    sl = slice(K_MIN - 1, NSTATES)
    rho = pearson(delta[sl], d[sl])

    rows = []
    for k in range(1, NSTATES + 1):
        rows.append(
            {
                "k": k,
                "mu_k": mus[k - 1],
                "kappa_mu_k": KAPPA * mus[k - 1],
                "gamma_k": gammas[k - 1],
                "d_k": d[k - 1],
                "E1_k": e1[k - 1],
                "delta_k": delta[k - 1],
                "turning_t_k": 0.5 * math.log(mus[k - 1] / Z0),
            }
        )
    with (OUT / "spectral_response_k1_40.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    sensitivities = []
    for sigma in (0.10, 0.25, 0.50, 1.00):
        for radius in ((250, 500, 1000, 2000) if sigma == PRIMARY_SIGMA else (2000,)):
            test_e1, test_delta = responses(mus, grid, densities, sigma, radius)
            test_rho = pearson(test_delta[sl], d[sl])
            sensitivities.append(
                {
                    "sigma": sigma,
                    "R": radius,
                    "rho_k5_40": test_rho,
                    "max_abs_delta_change_vs_primary": float(np.max(np.abs(test_delta - delta))),
                }
            )
            print(f"sensitivity sigma={sigma}, R={radius}, rho={test_rho:.12f}", flush=True)

    # Grid-spacing check for the primary convention.
    coarse_grid = grid[::2]
    coarse_densities = densities[:, ::2]
    _, coarse_delta = responses(mus, coarse_grid, coarse_densities, PRIMARY_SIGMA, PRIMARY_R)
    coarse_rho = pearson(coarse_delta[sl], d[sl])

    result = {
        "convention": {
            "domain": "L^2((0,infty),dt)",
            "left_boundary": "Dirichlet psi(0)=0",
            "right_boundary": "L^2 / K-decaying",
            "a": A,
            "kappa": KAPPA,
            "z0": Z0,
            "gaussian": "chi_sigma(u)=(2*pi*sigma^2)^(-1/2)*exp(-u^2/(2*sigma^2))",
            "primary_sigma": PRIMARY_SIGMA,
            "primary_R": PRIMARY_R,
            "k_range": [K_MIN, NSTATES],
            "grid_step": float(grid[1] - grid[0]),
        },
        "primary": {
            "rho": rho,
            "branch": "positive" if rho > 0.5 else ("negative" if rho < -0.5 else "neutral"),
            "mean_d": float(np.mean(d[sl])),
            "mean_delta": float(np.mean(delta[sl])),
            "positive_d_count": int(np.sum(d[sl] > 0)),
            "positive_delta_count": int(np.sum(delta[sl] > 0)),
            "same_sign_count": int(np.sum(d[sl] * delta[sl] > 0)),
            "count": len(d[sl]),
        },
        "normalization_checks": norm_checks,
        "coarse_grid_check": {
            "grid_step": float(coarse_grid[1] - coarse_grid[0]),
            "rho": coarse_rho,
            "rho_absolute_change": abs(coarse_rho - rho),
            "max_abs_delta_change": float(np.max(np.abs(coarse_delta - delta))),
        },
        "sensitivities": sensitivities,
    }
    (OUT / "spectral_response_summary.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(result, indent=2, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
