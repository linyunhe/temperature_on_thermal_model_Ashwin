# Retrieving temperature mapping based on Ashwin's thermal model
This is the python version and assume you have already install these libraries:\
[Spectral](http://www.spectralpython.net/), [Pillow](https://pillow.readthedocs.io/en/stable/), [NumPy](http://www.numpy.org/), [re](https://docs.python.org/3/library/re.html) and [SciPy](https://www.scipy.org/).

**Input**: Ashwin's model txt, albedo cube, thermal inertia image (.tiff)
**Output**: Temperature mapping based on Ashwin's thermal model for given albedo cube

There are two versions: one for jupyter notebook (Generate_Thermal_Map_txt.ipynb) and one for python script (thermal_map_basedon_Ashwin_model.py).

## Jupyter notebook
1. Download and open Generate_Thermal_Map_txt.ipynb.
2. Change the file names (both input and output) in the first five lines of the second cell.
3. Run the whole jupyter notebook.

## Python script
1. Download thermal_map_basedon_Ashwin_model.py.
2. Open command windown and go to the directory you save  thermal_map_basedon_Ashwin_model.py.
3. Type *python thermal_map_basedon_Ashwin_model.py* in the command line.
4. Follow the displayed instructions:

*What is your folder path:*

*What is the filename of albedo:*

*What is the filename of thermal inertia:*

*What is the filename of thermal model:*

*Save name of output temperature:*