Contribution Guidelines
-----------------------

Before contributing
-------------------

Welcome to einsteinpy-geodesics! Before contributing to the project,
make sure that you read our `code of conduct`_.

.. _`code of conduct`: https://github.com/einsteinpy/einsteinpy-geodesics/blob/master/CODE_OF_CONDUCT.rst

Contributing
------------

These are some succint steps to set up a development environment and contribute to EinsteinPy Geodesics:

1. `Install git <https://git-scm.com/>`_ on your computer.
2. `Register to GitHub <https://github.com/>`_.
3. `Fork einsteinpy_geodesics <https://help.github.com/articles/fork-a-repo/>`_.
4. `Clone your fork <https://help.github.com/articles/cloning-a-repository/>`_.
5. Install it in development mode, using:
   :code:`flit install --symlink /path/to/einsteinpy_geodesics/` (on *nix)
   or :code:`flit install --pth-file /path/to/einsteinpy_geodesics/` (on Windows). This means, that the
   installed code will change as soon as you change it in the download location.
6. Create a new branch from master: `git switch -c new-branch master`.
7. Make your code changes.
8. Check that your code follows the style guidelines of the project: `tox -e reformat && tox -e check`
9. Run the tests: `tox -e py37`. Change the version number according to the Python version, you are using.
10. `Push to your fork <https://help.github.com/articles/pushing-to-a-remote/>`_.
11. `Open a pull request! <https://help.github.com/articles/creating-a-pull-request/>`_


Reporting Bugs
--------------

If you find anything that doesn't work as expected or have suggestions, please refer to the `issue tracker`_ on GitHub.

.. _`issue tracker`: https://github.com/einsteinpy/einsteinpy-geodesics/issues


API Reference
-------------

Complete API Reference for the package can be accessed at `Read the Docs`_.

https://docs.geodesics.einsteinpy.org/en/latest/

.. _`Read the Docs`: https://readthedocs.org/
