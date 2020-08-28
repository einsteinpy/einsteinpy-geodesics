from pathlib import Path

from einsteinpy_geodesics.utils import _project_root


def test_project_root():
    root = _project_root()

    expected = Path.cwd() / "src"

    assert root == expected
