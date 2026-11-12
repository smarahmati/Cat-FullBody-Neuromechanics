"""Compiled activation/elastic prehistory, evaluated only before time zero."""

import numpy as np

from numba import njit

from .solve_elastic_muscle_equilibrium import solve_elastic_muscle_equilibrium


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=False)
def periodic_muscle_history_kernel(
    mtu,
    table,
    lopt,
    slack,
    params,
    e0,
    beta,
    time_constants,
    period,
    cycles,
):
    n, nm = mtu.shape
    dt = period / n
    a = np.zeros(nm)
    lf = np.maximum(0.21 * lopt, (mtu[0] - slack) / params[:, 9])
    before_a = a.copy()
    before_lf = lf.copy()
    for k in range(cycles * n):
        frame = k % n
        pos = frame / n * (len(table) - 1)
        left = int(pos)
        w = pos - left
        u = table[left] * (1 - w) + table[left + 1] * w
        factor = 0.5 + 1.5 * a
        tau = np.where(u > a, time_constants[:, 0] * factor, time_constants[:, 1] / factor)
        a = np.clip(a + dt * (u - a) / tau, 0.0, 1.0)
        lf, v, f, r, b = solve_elastic_muscle_equilibrium(
            mtu[(frame + 1) % n],
            lf,
            a,
            lopt,
            slack,
            params,
            e0,
            beta,
            dt,
        )
        if k == (cycles - 1) * n - 1:
            before_a = a.copy()
            before_lf = lf.copy()
    return a, lf, v, f, r, b, a - before_a, lf - before_lf
