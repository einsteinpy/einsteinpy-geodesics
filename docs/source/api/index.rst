API Reference
*************

Welcome to the API documentation of EinsteinPy Geodesics. You can find the API reference for the `solveSystem` method below. An in-depth description of this module can be found `here`_. If anything seems out of place, please open an `issue in the repo`_ .

.. _`here` : https://github.com/einsteinpy/einsteinpy-geodesics/README.md
.. _`issue in the repo` : https://github.com/einsteinpy/einsteinpy-geodesics


`einsteinpy_geodesics.solveSystem(q, p, params, end_lambda, step_size)`
#######################################################################

This module contains the python wrapper, that solves for Kerr (& Schwarzschild) Geodesics in Julia. This backend produces stable output. It is highly recommended to use this backend by setting `julia=True`, in the constructor call to ``einsteinpy.geodesic.*``.

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


