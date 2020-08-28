EinsteinPy Geodesics
====================

EinsteinPy Geodesics is an addon package for EinsteinPy, that wraps over Julia's 
excellent `DifferentialEquations.jl <https://diffeq.sciml.ai/stable/>`_
suite and provides a python interface to solve for geodesics in Kerr & Schwarzschild spacetime.
`EinsteinPy <https://einsteinpy.org/>`_ is an open source pure Python package, dedicated to problems arising
in General Relativity and Gravitational Physics. 
As with EinsteinPy, EinsteinPy Geodesics is released under the MIT license. The source code of 
`einsteinpy_geodesics` can be viewed `here <https://github.com/einsteinpy/einsteinpy-geodesics>`_.


This package makes use of the Kerr super-hamiltonian (See Gravitation Ch. 33, MTW),
and `DifferentialEquations.jl`'s `HamiltonianProblem` type to automatically derive the dynamical 
equations and solve for Kerr geodesics. Since, Schwarzschild spacetime is a limit of Kerr spacetime,
Schwarzschild geodesics can also be calculated. Below, we present some of the geodesic plots, made using
`einsteinpy` and `einsteinpy_geodesic`.

.. image:: _static/anim.gif
   :alt: Kerr Constant Radius Orbit Animation
   :align: center

.. image:: _static/drag.png
   :alt: Kerr Null-like Frame Dragging
   :width: 484px
   :align: center

.. image:: _static/precess.png
   :alt: Schwarzschild Precession
   :width: 484px
   :align: center


Release announcements and general discussion take place on our `mailing list`_
and `chat`_.

.. _`mailing list`: https://groups.io/g/einsteinpy-dev
.. _`chat`: https://riot.im/app/#/room/#einsteinpy:matrix.org


The `source code`_, `issue tracker`_ and `wiki`_ are hosted on GitHub, and all
contributions and feedback are more than welcome.

.. image:: https://img.shields.io/badge/launch-binder-e66581.svg?style=flat-square
   :target: https://beta.mybinder.org/v2/gh/einsteinpy/einsteinpy/master?filepath=index.ipynb

.. _`source code`: https://github.com/einsteinpy-geodesics/einsteinpy
.. _`issue tracker`: https://github.com/einsteinpy/einsteinpy-geodesics/issues
.. _`wiki`: https://github.com/einsteinpy/einsteinpy-geodesics/wiki/

-----

Contents
--------

.. toctree::
   :maxdepth: 2

   dev_guide
   api/index
   codeofconduct
