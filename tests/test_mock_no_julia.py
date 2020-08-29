import pytest
import numpy as np

from numpy.testing import assert_allclose
from unittest.mock import patch

import einsteinpy_geodesics


@pytest.fixture
def input_timelike():
    # Equatorial Spiral Capture
    q = [4.0, np.pi / 2, 0.0]
    p = [0.0, 0.0, 3.5]
    params = [0.0, 0.9476286192385706, -1.0]
    end_lambda = 1.0
    step_size = 0.05

    return q, p, params, end_lambda, step_size


def sb_call_test(cmd):
    raise OSError


def test_wrapper_mock_no_julia(input_timelike):
    q, p, params, end_lambda, step_size = input_timelike

    with patch('einsteinpy_geodesics.geodesics_wrapper.sb.call', new=sb_call_test):
        try:
            lambdas, vecs = einsteinpy_geodesics.solveSystem(q, p, params, end_lambda, step_size)
            assert False
        except OSError:
            assert True
