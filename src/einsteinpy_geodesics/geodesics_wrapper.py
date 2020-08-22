try:
    from julia import Main

except ImportError:
    raise ImportError(
        """
        Could not import 'julia'. 
        Make sure 'julia' is installed in your system and added to path.
        Refer: https://julialang.org/downloads/platform/.
        Also, ensure that PyJulia is installed by entering 
        'python -m pip install julia' in a terminal window.
        Refer: https://pyjulia.readthedocs.io/en/latest/installation.html
        """
    )

Main.include("src/einsteinpy_geodesics/KerrSolver.jl")


def SolveSystem(q, p, params, end_lambda, step_size):
    """
    Wrapper to `KerrSolver.solveSystem`, from the Julia code

    Parameters
    ----------
    q : array_like
        Length-3 Array, containing the initial 3-Position
    p: array_like
        Length-3 Array, containing the initial Covariant 3-Momentum
    params : array_like
        Length-4 Array, containing - 
        Black Hole Spin Parameter, `a`,
        Test Particle Energy, `E`,
        Test Particle Mass, `mu`,
        Norm of tangent vector (4-Velocity/4-Momentum), `fac`
    end_lambda : float
            Affine Parameter value, where integration will end
            Equivalent to Proper Time for Timelike Geodesics
    step_size : float, optional
        Size of each geodesic integration step
        A fixed-step, symplectic VerletLeapfrog integrator is used

    Returns
    -------
    retcode : str
        Return status code of the solver
    lambdas : ~numpy.ndarray
        Array, containing affine parameter values, where integration was performed
    vecs : ~numpy.ndarray
        2D Array, containing integrated 3-Positions and Covariant 3-Momenta

    """
    retcode, lambdas, vecs = Main.KerrSolver.solveSystem(
        q, p, params, end_lambda, step_size
    )

    return retcode, lambdas, vecs
