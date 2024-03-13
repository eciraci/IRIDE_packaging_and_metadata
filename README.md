IRIDE Ground Motion Segment - Post-Processing Tools
----

This repository contains a set of sample scripts and utility functions 
employed to post-process and package geospatial products for the IRIDE Service 
Segment Lot-2.

---
[![Language][]][1]
[![License][]][1]

---
#### Sentinel-1 Processing

Ad-hoc processing of Sentinel-1 data.

- **_index_bursts.py_** - Identify Sentinel-1 bursts covering the selected area of interest.  Save the generated index to an ESRI shapefile.
- **_index_tiles.py_** - IdentifyIRIDE L3 Tiles covering the selected area of interest.  Save the generated index to an ESRI shapefile.
- **_merge_bursts.py_** - Merge PS belonging to all bursts belonging to the same track that have been indexed by index_bursts.py. 
- **_merge_tiles.py_** - Merge 2D Deformation belonging to all tiles intersecting the AOI and that have been indexed by index_tiles.py.

----
#### COSMO-SkyMed Processing
TBD

----
#### SAOCOM Processing
TBD

----

**Install Python Dependencies**:

1. Setup minimal **conda** installation using [Miniconda][]

2. Setup a Python Virtual Environment

    > -   Creating an environment with commands ([Link][]);
    > -   Creating an environment from an environment.yml file
    >     ([Link][2]);


----
#### PYTHON DEPENDENCIES:
- [gdal: Python's GDAL binding.][]
- [fiona: Fiona is GDAL’s neat and nimble vector API for Python programmers.][]
- [numpy: The fundamental package for scientific computing with Python.][]
- [pandas: Python Data Analysis Library.][]
- [geopandas: add support for geographic data to pandas objects.][]
- [lxml: XML and HTML with Python.][]


---
## License

The content of this project is licensed under the [Creative Commons
Attribution 4.0 Attribution license][] and the source code is licensed
under the [MIT license][].


[Language]: https://img.shields.io/badge/python-%3E%3D%203.10-blue
[License]: https://img.shields.io/bower/l/MI
[1]: ..%20image::%20https://www.python.org/
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Link]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
[2]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
[xarray: Labelled multi-dimensional arrays in Python.]:https://docs.xarray.dev
[rasterio: access to geospatial raster data]:https://rasterio.readthedocs.io/en/latest/
[gdal: Python's GDAL binding.]: https://gdal.org/index.html
[tqdm: A Fast, Extensible Progress Bar for Python and CLI.]: https://github.com/tqdm/tqdm
[necdft4: Provides an object-oriented python interface to the netCDF version 4 library.]:https://pypi.org/project/netCDF4/
[fiona: Fiona is GDAL’s neat and nimble vector API for Python programmers.]:https://fiona.readthedocs.io/en/latest/
[numpy: The fundamental package for scientific computing with Python.]:https://numpy.org
[PyTMD: Python package for the analysis of tidal data.]: https://github.com/tsutterley/pyTMD
[pandas: Python Data Analysis Library.]:https://pandas.pydata.org/
[geopandas: add support for geographic data to pandas objects.]:https://geopandas.org/en/stable/
[matplotlib: Library for creating static, animated, and interactive visualizations in Python.]:https://matplotlib.org
[lxml: XML and HTML with Python.]:https://lxml.de/
[alphashape: Alpha Shape Toolbox.]:https://pypi.org/project/alphashape/
[Creative Commons Attribution 4.0 Attribution license]: https://creativecommons.org/licenses/by/4.0/
[MIT license]: LICENSE