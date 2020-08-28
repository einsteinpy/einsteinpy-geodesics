"""
Wrapper to Julia code, in ``run.jl`` and ``KerSolver.jl``

This backend produces stable output. It is highly recommended to
use this backend by setting `julia=True`, in the constructor call to
``einsteinpy.geodesic.*``.

Parameters
----------
q : array_like
    Length-3 Array, containing the initial 3-Position
p : array_like
    Length-3 Array, containing the initial Covariant 3-Momentum
params : array_like
    Length-3 Array, containing Black Hole Spin Parameter, `a`, Test Particle Energy, `E` and
    Test Particle Rest Mass, `mu`
end_lambda : float
    Affine Parameter value, where integration will end
step_size : float
    Step Size (Fixed)

Returns
-------
lambdas : numpy.ndarray
    Array, containing affine parameter values, where integration was performed
vecs : numpy.ndarray
    2D Array, containing integrated 3-Positions and Covariant 3-Momenta

Raises
------
OSError
    If ``julia`` is not found on system path

"""

import subprocess as sb
import warnings

import numpy as np
import re

from .utils import _project_root


def solveSystem(q, p, params, end_lambda, step_size):
    """
    Wrapper to Julia code, in ``run.jl`` and ``KerSolver.jl``

    This backend produces stable output. It is highly recommended to
    use this backend by setting `julia=True`, in the constructor call to
    ``einsteinpy.geodesic.*``.

    Parameters
    ----------
    q : array_like
        Length-3 Array, containing the initial 3-Position
    p : array_like
        Length-3 Array, containing the initial Covariant 3-Momentum
    params : array_like
        Length-3 Array, containing Black Hole Spin Parameter, `a`, Test Particle Energy, `E` and
        Test Particle Rest Mass, `mu`
    end_lambda : float
        Affine Parameter value, where integration will end
    step_size : float
        Step Size (Fixed)

    Returns
    -------
    lambdas : numpy.ndarray
        Array, containing affine parameter values, where integration was performed
    vecs : numpy.ndarray
        2D Array, containing integrated 3-Positions and Covariant 3-Momenta

    Raises
    ------
    OSError
        If ``julia`` is not found on system path

    """
    q1, q2, q3 = q
    p1, p2, p3 = p
    a, E, mu = params

    # Arguments for julia script
    args = f"{q1} {q2} {q3} {p1} {p2} {p3} {a} {E} {end_lambda} {step_size}".split(" ")

    # Checking, if julia is callable
    try:
        sb.call(["julia"])
    except OSError:
        raise OSError(
            """
            Could not call 'julia'. 
            Make sure 'julia' is installed in your system and added to path.
            Refer: https://julialang.org/downloads/platform/.
            Also, ensure that 'DifferentialEquations.jl' and 'ODEInterfaceDiffEq.jl' 
            are installed in julia. You can install them by typing
            `using Pkg; Pkg.add("DifferentialEquations"); Pkg.add("ODEInterfaceDiffEq");`
            in a julia terminal.
            """
        )

    # Running script
    script_abspath = str(_project_root() / "einsteinpy_geodesics/julia_backend/run.jl")
    jl_out = sb.check_output(["julia", script_abspath] + args)

    # Sanitizing output and formatting it to a list
    jl_out_list = re.findall(r"['\"](.*?)['\"]", str(jl_out.decode("unicode-escape")))
    retcode, out_path = jl_out_list

    lambdas = np.loadtxt(out_path + "\\lambdas.csv", delimiter=",")
    vecs = np.loadtxt(out_path + "\\vecs.csv", delimiter=",")

    if retcode == "Terminated":
        warnings.warn("Test particle has reached the Event Horizon. ", RuntimeWarning)

    return lambdas, vecs
