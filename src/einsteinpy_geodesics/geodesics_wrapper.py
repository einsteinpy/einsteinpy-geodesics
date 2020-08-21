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

Main.include("KerrSolver.jl")

def SolveSystem(q, p, params, end_lambda, step_size):
    retcode, lambdas, vecs = Main.solveSystem(
        q,
        p,
        params,
        end_lambda,
        step_size
    )

    return retcode, lambdas, vecs
