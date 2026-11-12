"""Shared constitutive constants used by the actual compiled equations.

Edit, then start a NEW run.py process. Dependent kernels compile afresh so
edits cannot be masked by a stale Numba cache. These are curve-law constants,
not individually measured parameters of each cat muscle. Defaults preserve
the previous numerical model. See Documentation/model_methods.html.
"""

# Source MATLAB active force-length shape (original 1.55 and 0.55).
ACTIVE_LENGTH_POWER = 1.55
# Set ACTIVE LENGTH WIDTH.
ACTIVE_LENGTH_WIDTH = 0.55
# Published parallel elastic curve: Prilutsky et al. (2016), Table 10.3,
# DOI 10.1007/978-1-4939-3267-2_10; Rahmati et al. (2025), Table 3,
# DOI 10.1113/JP287448. Original coefficients are 0.0075 and 11.6.
# This implementation rectifies the curve to zero for l_f / l_opt <= 1.
PASSIVE_LENGTH_SCALE = 0.0075
# Set PASSIVE LENGTH EXPONENT.
PASSIVE_LENGTH_EXPONENT = 11.6
# Set PASSIVE EXPONENT CAP.
PASSIVE_EXPONENT_CAP = 50.0  # Numerical overflow guard; original 50.
# De Groote 2016 / OpenSim corrected velocity coefficients. Original rounded
# paper d1=-0.318, d2=-8.149, d3=-0.374, d4=0.886.
FV_D1 = -0.3211346127989808
# Set FV D2.
FV_D2 = -8.149
# Set FV D3.
FV_D3 = -0.374
# Set FV D4.
FV_D4 = 0.8825327733249912
# Current exponential-to-linear tendon law: original toe curvature 3.0.
# The 0.33 toe force and toe-length ratio are coupled to this specific law;
# changing its shape requires continuity/slope checks, not arbitrary tuning.
TENDON_TOE_CURVATURE = 3.0
# Contact assumption: dashpot reaches full strength at 1 mm indentation.
# This is an engineering regularization, not a measured cat tissue value.
SHEAR_DAMPING_DEPTH_M = 0.001
# Numerical collapse criteria, not forces or experimentally identified limits.
FALL_PELVIS_HEIGHT_M = 0.10
# Set FALL ROOT PITCH RAD.
FALL_ROOT_PITCH_RAD = 1.0
