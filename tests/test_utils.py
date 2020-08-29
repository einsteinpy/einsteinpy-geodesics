from pathlib import Path

import einsteinpy_geodesics.utils as egu


def test_project_root():
    root = egu._project_root()

    expected = Path(egu.__file__).parent.parent

    assert root == expected
