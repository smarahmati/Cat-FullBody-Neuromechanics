"""Model 3 and forelimb source pulley tangents; no fitted attachments."""

import math, numpy as np

from numba import njit

from .route_two_joint_muscle import route_two_joint_muscle


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=True)
def calculate_muscle_route_points(q, meta, geom):
    out = np.empty((len(meta), 2))
    for k in range(len(meta)):
        adr, j1, j2, fore, mono = meta[k, :5]
        ls = geom[k, 10]
        g = geom[k, :10]
        a = (
            (math.pi + q[adr + j1] if j1 == 0 else math.pi - q[adr + j1])
            if fore
            else (
                -q[adr + j1]
                if j1 == 0
                else (math.pi + q[adr + j1] if j1 == 1 else math.pi - q[adr + j1])
            )
        )
        if mono:
            a1, a2, p1, p2, r1, f1, n1 = g[:7]
            beta = f1 * math.acos(max(-1.0, min(1.0, r1 / a1))) + p1
            beta2 = -f1 * math.acos(max(-1.0, min(1.0, r1 / a2))) + p2
            theta = abs(f1 - n1) * math.pi + f1 * n1 * (a - n1 * (beta - beta2))
            ang = math.pi + beta + f1 * max(theta, 0.0) / 2
            out[k, 0] = r1 * 1.05 * math.cos(ang) + ls
            out[k, 1] = r1 * 1.05 * math.sin(ang)
        else:
            b = (
                (math.pi + q[adr + j2] if j2 == 0 else math.pi - q[adr + j2])
                if fore
                else (
                    -q[adr + j2]
                    if j2 == 0
                    else (math.pi + q[adr + j2] if j2 == 1 else math.pi - q[adr + j2])
                )
            )
            out[k] = route_two_joint_muscle(g, a, b, ls)[1]
    return out
