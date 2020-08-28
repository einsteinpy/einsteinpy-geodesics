import os
import tempfile
import warnings
from pathlib import Path

import numpy as np
import pytest
from numpy.testing import assert_allclose

import einsteinpy_geodesics as epyg


@pytest.fixture
def input_timelike():
    # Equatorial Spiral Capture
    q = [4.0, np.pi / 2, 0.0]
    p = [0.0, 0.0, 3.5]
    params = [0.0, 0.9476286192385706, -1.0]
    end_lambda = 1.0
    step_size = 0.05

    return q, p, params, end_lambda, step_size


@pytest.fixture
def input_nulllike():
    # Reverse & Capture
    q = [2.5, np.pi / 2, 0.0]
    p = [0.0, 0.0, -2.0]
    params = [0.9, 0.1878809905821554, 0.0]
    end_lambda = 10.0
    step_size = 0.05

    return q, p, params, end_lambda, step_size


def test_csvs_exist_after_julia_call(input_timelike):
    q, p, params, end_lambda, step_size = input_timelike

    lambdas, vecs = epyg.solveSystem(q, p, params, end_lambda, step_size)

    out_path = Path(tempfile.gettempdir()) / "epy_geod_jl_temp"

    list_of_files = os.listdir(out_path)

    assert "lambdas.csv" in list_of_files
    assert "vecs.csv" in list_of_files


def test_return_types(input_timelike):
    q, p, params, end_lambda, step_size = input_timelike

    lambdas, vecs = epyg.solveSystem(q, p, params, end_lambda, step_size)

    assert type(lambdas) == np.ndarray
    assert type(vecs) == np.ndarray
    assert type(lambdas[-1]) in (float, np.float64)
    assert type(vecs[-1, -1]) in (float, np.float64)


def test_geodesic_attributes(input_nulllike):
    q, p, params, end_lambda, step_size = input_nulllike

    lambdas, vecs = epyg.solveSystem(q, p, params, end_lambda, step_size)

    assert lambdas.shape[0] == vecs.shape[0]
    assert vecs.shape[1] == 6


def test_integration_termination_callback(input_nulllike):
    q, p, params, end_lambda, step_size = input_nulllike

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")

        lambdas, vecs = epyg.solveSystem(q, p, params, end_lambda, step_size)

        assert len(w) == 1  # 1 warning to be shown
        assert issubclass(w[-1].category, RuntimeWarning)


def test_motion_constant_timelike(input_timelike):
    q, p, params, end_lambda, step_size = input_timelike

    L = p[-1]

    lambdas, vecs = epyg.solveSystem(q, p, params, end_lambda, step_size)

    assert_allclose(L, vecs[:, 5], atol=1e-3, rtol=1e-3)


def test_motion_constants_nulllike(input_nulllike):
    q, p, params, end_lambda, step_size = input_nulllike

    L = p[-1]

    lambdas, vecs = epyg.solveSystem(q, p, params, end_lambda, step_size)

    assert_allclose(L, vecs[:, 5], atol=1e-3, rtol=1e-3)
