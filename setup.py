import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="einsteinpy_geodesics", # Replace with your own username
    version="0.0.1",
    author="JeS24",
    author_email="jyotirmaya@einsteinpy.org",
    description="Python wrapper for a Julia solver for geodesics in the Kerr family of spacetimes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="??",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)