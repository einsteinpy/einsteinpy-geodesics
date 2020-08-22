import numpy as np
import pytest
from numpy.testing import assert_allclose

import einsteinpy_geodesics as epyg


@pytest.fixture
def input_timelike():
    # Equatorial Spiral Capture
    q = [4.0, np.pi / 2, 0.0]
    p = [0.0, 0.0, 3.5]
    params = [0.0, 0.9476286192385706, 1.0, 0.5]
    end_lambda = 150.0
    step_size = 0.0005

    return q, p, params, end_lambda, step_size


@pytest.fixture
def input_nulllike():
    # Reverse & Capture
    q = [2.5, np.pi / 2, 0.0]
    p = [0.0, -0.2, -2.0]
    params = [0.9, 0.1878809905821554, 0.0, 0.0]
    end_lambda = 90.0
    step_size = 0.0005

    return q, p, params, end_lambda, step_size


def test_return_types(input_timelike):
    q, p, params, end_lambda, step_size = input_timelike

    retcode, lambdas, vecs = epyg.SolveSystem(q, p, params, end_lambda, step_size)

    assert type(retcode) == str
    assert type(lambdas) == np.ndarray
    assert type(vecs) == np.ndarray
    assert type(lambdas[-1]) == np.float64
    assert type(vecs[-1, -1]) == np.float64


def test_integration_termination_callback(input_timelike):
    q, p, params, end_lambda, step_size = input_timelike

    retcode, lambdas, vecs = epyg.SolveSystem(q, p, params, end_lambda, step_size)

    assert retcode == "Terminated"


def test_motion_constant_timelike(input_timelike):
    q, p, params, end_lambda, step_size = input_timelike

    L = p[-1]

    retcode, lambdas, vecs = epyg.SolveSystem(q, p, params, end_lambda, step_size)

    assert_allclose(L, vecs[:, 5], atol=1e-3, rtol=1e-3)


def test_motion_constants_nulllike(input_nulllike):
    q, p, params, end_lambda, step_size = input_nulllike

    L = p[-1]

    retcode, lambdas, vecs = epyg.SolveSystem(q, p, params, end_lambda, step_size)

    assert_allclose(L, vecs[:, 5], atol=1e-3, rtol=1e-3)
