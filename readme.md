# Retrieving temperature mapping based on Ashwin's thermal model
This is the python version and assume you have already installed these libraries:\
[Spectral](http://www.spectralpython.net/), [Pillow](https://pillow.readthedocs.io/en/stable/), [NumPy](http://www.numpy.org/), [re](https://docs.python.org/3/library/re.html) and [SciPy](https://www.scipy.org/).

**Input**: Ashwin's model txt (multiple degrees), expected viewing degree and albedo cube of one scene, thermal inertia image (.tiff) overlapping this scene

**Output**: Temperature mapping based on Ashwin's thermal model for this scene

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

*What is your folder path:* Directory for all files

*What is the filename of albedo:* Lambert albedo cube for one scene

*Which band is selected out of albedo file:* The selected band number (starting from 0)

*What is the filename of thermal inertia:* Thermal inertia overlapped with the previous Lambert albedo cube

*What is the filename of thermal model 1:* Thermal model 1 at degree 1

*What is the degree of thermal model 1:* Degree 1 for thermal model 1

*What is the filename of thermal model 2:* Thermal model 2 at degree 2

*What is the degree of thermal model 2:* Degree 2 for thermal model 2

*What is your expected degree:* Expected viewing degree of this scene

*Save name of output temperature:* Name of output file