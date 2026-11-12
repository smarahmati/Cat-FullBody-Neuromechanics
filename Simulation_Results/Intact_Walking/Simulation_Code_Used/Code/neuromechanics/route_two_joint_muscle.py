"""Route two joint muscle.

Inputs/outputs: see the named function arguments and returned values.
Lengths use metres, time seconds, force newtons, and angles radians unless stated.
See Documentation/model_methods.html for equations and parameter definitions.
"""

import math, numpy as np

from numba import njit

from .clipped_acos import clipped_acos as acos

from .polar_point import polar_point as polar


# Compile this numerical function for repeated evaluations; its equations stay unchanged.
@njit(cache=True)
def route_two_joint_muscle(g, a, b, ls):
    """Length and intermediate tangent point, translated from the MATLAB cases."""
    a1, a2, p1, p2, r1, f1, n1 = g[:7]
    beta1 = f1 * acos(r1 / a1) + p1
    r2, f2, n2 = g[7:10]
    beta2 = -f2 * acos(r2 / a2) + p2
    h1 = math.sqrt(ls * ls - (f1 * r1 - f2 * r2) ** 2)
    rho1 = -f1 * acos((r2 * r2 + h1 * h1 - r1 * r1 - ls * ls) / (-2 * r1 * ls))
    rho2 = f2 * acos((r1 * r1 + h1 * h1 - r2 * r2 - ls * ls) / (-2 * r2 * ls))
    t1 = abs(f1 - n1) * math.pi + f1 * n1 * (a - n1 * (beta1 - rho1))
    t2 = abs(f2 - n2) * math.pi + f2 * n2 * (b + n2 * (beta2 - rho2))
    O = polar(a1, math.pi + n1 * (math.pi - a) + p1)
    I = np.array([ls, 0.0]) + polar(a2, n2 * (b - math.pi) + p2)
    if t1 >= 0 and t2 >= 0:
        P = polar(r1, rho1)
        Q = np.array([ls, 0.0]) + polar(r2, math.pi + rho2)
        L = (
            math.sqrt(max(0, a1 * a1 - r1 * r1))
            + r1 * t1
            + h1
            + r2 * t2
            + math.sqrt(max(0, a2 * a2 - r2 * r2))
        )
    elif t1 < 0 and t2 >= 0:
        h4 = math.sqrt(ls * ls + a1 * a1 - 2 * a1 * ls * math.cos(a - n1 * p1))
        rm = f2 * abs(
            f1 * acos((a1 * a1 - ls * ls - h4 * h4) / (-2 * ls * h4))
            + f2 * acos(r2 / h4)
        )
        tm = abs(f2 - n2) * math.pi + f2 * n2 * (b + n2 * (beta2 - rm))
        P = O
        Q = np.array([ls, 0.0]) + polar(r2, math.pi + rm)
        if tm < 0:
            Q = I
        L = math.sqrt(h4 * h4 - r2 * r2) + r2 * tm + math.sqrt(max(0, a2 * a2 - r2 * r2))
    elif t1 >= 0 and t2 < 0:
        h5 = math.sqrt(ls * ls + a2 * a2 - 2 * a2 * ls * math.cos(b + n2 * p2))
        rm = -f1 * abs(
            f1 * acos((a2 * a2 - ls * ls - h5 * h5) / (-2 * ls * h5))
            + f2 * acos(r1 / h5)
        )
        tm = abs(f1 - n1) * math.pi + f1 * n1 * (a - n1 * (beta1 - rm))
        P = polar(r1, rm)
        Q = I
        if tm < 0:
            P = O
        L = math.sqrt(max(0, a1 * a1 - r1 * r1)) + r1 * tm + math.sqrt(h5 * h5 - r1 * r1)
    else:
        P = O
        Q = I
        h6 = a1 * math.cos(math.pi - a + n1 * p1)
        h7 = a2 * math.cos(math.pi - b - n2 * p2)
        L = math.sqrt(
            (
                f1 * math.sqrt(max(0, a1 * a1 - h6 * h6))
                - f2 * math.sqrt(max(0, a2 * a2 - h7 * h7))
            )
            ** 2
            + (ls + h6 + h7) ** 2
        )
    return L, (P + Q) / 2, (t1, t2)
