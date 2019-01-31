
# coding: utf-8

# In[2]:


import spectral as spy
from PIL import Image
import numpy as np
import re
import matplotlib.pyplot as plt
from scipy import interpolate

folder = input("What is your folder path:")
albedo_filename = input("What is the filename of albedo:")
TI_filename = input("What is the filename of thermal inertia:")
thermal_model_filename = input("What is the filename of thermal model:")
T_savefilename = input("Save name of output temperature:")

albedo_file = folder+'/'+albedo_filename+'.hdr'
band_num = 400
TI_file = folder+'/'+TI_filename+'.tiff'
thermal_model_file = folder+'/'+thermal_model_filename+'.txt'
T_savefile = folder+'/'+T_savefilename


# Read albedo and TI
albedo = spy.open_image(albedo_file).read_band(band_num);
TI = Image.open(TI_file)
TI_lon_start, TI_lat_start = TI.tag[33922][3:5]
TI_lon_del, TI_lat_del = TI.tag[33550][0:2]
TI = np.array(TI)
TI_num_row, TI_num_col = TI.shape
fh = open(albedo_file)
for line in fh:
    # in python 2
    # print line
    # in python 3
    if "map info" in line:
        lon_start, lat_start, lon_del, lat_del = re.findall("[-+]?\d*\.\d+|\d+", line)[5:9]
        lon_start = float(lon_start)
        lat_start = float(lat_start)
        lon_del = float(lon_del)
        lat_del = float(lat_del)
        break
fh.close()
print("TI start long: "+str(TI_lon_start)+" and delta: "+str(TI_lon_del))
print("TI start lat: "+str(TI_lat_start)+" and delta: "+str(TI_lat_del))
print("Albedo start long: "+str(lon_start)+" and delta: "+str(lon_del))
print("Albedo start lat: "+str(lat_start)+" and delta: "+str(lat_del))

# Read THERMAL_MODEL
model = open(thermal_model_file)
start_flag = False
model_table = list()
for line in model:
    if start_flag:
        tmp_albedo, tmp_ti,tmp_t = re.findall("\d+\.\d+", line)
        model_table.append([float(tmp_albedo),float(tmp_ti),float(tmp_t)])
    elif "Columns are Albedo" in line:
        start_flag = True

# Map TI to albedo domain
OFFSET = 8145529
print('Mapping TI to albedo domain...')
num_row,num_col = albedo.shape
mapped_TI = np.zeros((num_row,num_col))
TI_lat_end = TI_lat_start-TI_lat_del*(TI_num_row-1)
TI_lon_end = TI_lon_start+TI_lon_del*(TI_num_col-1)
for i in range(num_row):
    tmp_lat = lat_start-i*lat_del
    if (tmp_lat<=TI_lat_start and tmp_lat>=TI_lat_end):
        for j in range(num_col):
            if not np.isnan(albedo[i,j]):
                tmp_lon = lon_start+j*lon_del+OFFSET
                if(tmp_lon>= TI_lon_start and tmp_lon <= TI_lon_end):
                    mapped_TI[i,j] = TI[round((TI_lat_start-tmp_lat)/TI_lat_del),round((tmp_lon-TI_lon_start)/TI_lon_del)]
print('Mapping TI to albedo domain...done!')                    
# Interpolate thermal model                    
model_table = np.array(model_table)
albedo_axis = model_table[:,0]
TI_axis = model_table[:,1]
T_axis = model_table[:,2]
f = interpolate.interp2d(albedo_axis, TI_axis, T_axis, kind='cubic')
# For all pixels
print('Retrieving temperature map...')
T_res = np.zeros((num_row,num_col))
for i in range(num_row):
    for j in range(num_col):
        if not np.isnan(albedo[i,j]) and mapped_TI[i,j]!=0:
            T_res[i,j] = f(albedo[i,j],mapped_TI[i,j])
print('Retrieving temperature map...done!')            
plt.imshow(T_res)
spy.envi.save_image(T_savefile+'.hdr',T_res,force = True)
