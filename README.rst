.. einsteinpy

.. image:: https://blog.einsteinpy.org/img/logo.png
   :target: https://einsteinpy.org/
   :alt: EinsteinPy Logo
   :width: 675px
   :align: center

.. |mailing| image:: https://img.shields.io/badge/mailing%20list-groups.io-8cbcd1.svg?style=flat-square
   :target: https://groups.io/g/einsteinpy-dev

.. |gitter| image:: https://img.shields.io/gitter/room/EinsteinPy-Project/EinsteinPy.svg?logo=gitter&style=flat-square
   :alt: Join the chat at https://gitter.im/EinsteinPy-Project/EinsteinPy
   :target: https://gitter.im/EinsteinPy-Project/EinsteinPy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |riotchat| image:: https://img.shields.io/matrix/einsteinpy:matrix.org.svg?logo=riot&style=flat-square
   :target: https://riot.im/app/#/room/#einsteinpy:matrix.org

.. |doi| image:: https://zenodo.org/badge/168302584.svg?style=flat-square
   :target: https://zenodo.org/badge/latestdoi/168302584

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
   :target: https://github.com/einsteinpy/einsteinpy-geodesics/blob/master/COPYING

.. |docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat-square
   :target: https://docs.geodesics.einsteinpy.org/en/latest/



:Name: EinsteinPy Geodesics
:Website: https://docs.geodesics.einsteinpy.org/en/latest/
:Version: 0.1.dev0

|mailing| |gitter| |riotchat| |license| |docs|

EinsteinPy Geodesics is an addon package for EinsteinPy, that wraps over Julia's 
excellent `DifferentialEquations.jl <https://diffeq.sciml.ai/stable/>`_
suite and provides a python interface to solve for geodesics in Kerr & Schwarzschild spacetime.
`EinsteinPy <https://einsteinpy.org/>`_ is an open source pure Python package, dedicated to problems arising
in General Relativity and Gravitational Physics. 
As with EinsteinPy, EinsteinPy Geodesics is released under the MIT license.

Documentation
=============

|docs|

Complete documentation for this module can be accessed at `<https://docs.geodesics.einsteinpy.org/en/latest/>`_ (Courtesy: `Read the Docs`_).

.. _`Read the Docs`: https://readthedocs.org/

Requirements
============

EinsteinPy Geodesics requires `Python >= 3.7`, `Julia >= 1.5` and the following Julia packages:

* Julia
   * `DifferentialEquations.jl >= 6.15`
   * `ODEInterfaceDiffEq.jl >= 3.7`

Installation
============

First, ensure that, Julia is installed in your system and added to `PATH`. See `<https://julialang.org/downloads/platform/>`_ 
for platform specific binaries and installation instructions. `einsteinpy_geodesics` also requires `DifferentialEquations.jl` 
and `ODEInterfaceDiffEq.jl`. You can add them, like so::
   
   $ julia
   julia> using Pkg
   julia> Pkg.add("DifferentialEquations")
   julia> Pkg.add("ODEInterfaceDiffEq")


Finally, `einsteinpy_geodesics` can be installed in the most intuitive way::


   $ pip install einsteinpy_geodesics


For using this package, we strongly recommend you to use EinsteinPy Core package along with it.

Alternatively, you can install the package from source, by cloning `einsteinpy_geodesics <https://github.com/einsteinpy/einsteinpy-geodesics/>`_,
and typing in the following, in a shell (in Linux/macOS)::

   $ flit install --symlink /path/to/einsteinpy_geodesics/

Or, on Windows::

   $ flit install --pth-file /path/to/einsteinpy_geodesics/


Problems
========

If the installation fails or you find something, that doesn't work as expected,
please open an issue in the `issue tracker`_.

.. _`issue tracker`: https://github.com/einsteinpy/einsteinpy-geodesics/issues

Contributing
============

EinsteinPy is a community project, hence all contributions are more than
welcome! For more information, head to `CONTRIBUTING.rst`_, that also 
contains the developer documentation.

.. _`CONTRIBUTING.rst`: https://github.com/einsteinpy/einsteinpy-geodesics/blob/master/CONTRIBUTING.rst


Support
=======

|mailing|

Release announcements and general discussion take place on our `mailing list`_.
Feel free to join!

.. _`mailing list`: https://groups.io/g/einsteinpy-dev

https://groups.io/g/einsteinpy-dev

Please join our `[matrix]`_ channel or `gitter`_ chat room for further queries.

.. _`[matrix]`: https://matrix.to/#/#einsteinpy:matrix.org

.. _`gitter`: https://gitter.im/EinsteinPy-Project/EinsteinPy

If you still have a doubt, write a mail directly to `all@einsteinpy.org <mailto:all@einsteinpy.org>`_.

Citing
======

If you use EinsteinPy or EinsteinPy Geodesics in your project, please
`drop us a line <mailto:all@einsteinpy.org>`_.

You can also use the DOI to cite it in your publications. This is the latest
one:

|doi|

And this is an example citation format::

 Shreyas Bapat et al. (2019). EinsteinPy: einsteinpy 0.1.0. Zenodo. 10.5281/zenodo.2582388


License
=======

|license|

EinsteinPy and hence, EinsteinPy Geodesics, is released under the MIT license, hence allowing commercial
use of the library. Please refer to `COPYING`_.

.. _`COPYING`: https://github.com/einsteinpy/einsteinpy-geodesics/blob/master/COPYING
