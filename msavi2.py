#!/usr/bin/env python
# coding: utf-8

# In[90]:


import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import os
import fiona
import rasterio
import rasterio.mask
from osgeo import ogr
import geopandas as gpd
from shapely.geometry import Polygon
import subprocess


# In[86]:



band4 = rasterio.open('LC08_L1TP_148039_20190528_20200828_02_T1_B4.TIF') # read band 4 tiff file to band4 variable
band5 = rasterio.open('LC08_L1TP_148039_20190528_20200828_02_T1_B5.TIF') # read band 5 tiff file to band5 variable
red = band4.read(1).astype('float64') #read band4 varable as float 64 and store that to varable red
nir = band5.read(1).astype('float64') #read band5 varable as float 64 and store that to varable nir


# In[89]:


def msavi2():
    msavi = (2 * nir + 1 - np.sqrt((2*nir+1)**2 - 8 * (nir - red))) / 2  #formula for canculating msavi
    msaviImage = rasterio.open('msaviImage.tiff','w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64') #provide crs, width, height, type information to raster
    
    msaviImage.write(msavi,1) # write raster to a file
    msaviImage.close()
    


# In[70]:


def location1shp():
    
    lon_point_list = [75.45157492160797, 75.4524278640747, 75.45236885547638, 75.45157492160797] # logitude values
    lat_point_list = [30.634404129904425, 30.63372099804389, 30.634399514164798, 30.634404129904425] # latitute values to list

    polygon_geom = Polygon(zip(lon_point_list, lat_point_list)) 
    
    crs = {'init': 'epsg:4326'} # Assign CRS 
    
    polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])   #Read data in Geodataframe    

    polygon.to_file(filename='polygon_loc1.shp', driver="ESRI Shapefile") # Export data to Shapefile
    


# In[71]:


def location2shp():
    
    lon_point_list = [85.85622847080231, 85.85590660572052, 85.85663080215454, 85.85686147212981, 85.85622847080231]
    lat_point_list = [26.09425078918021, 26.093581136401006, 26.09337879451938, 26.094009907326967, 26.09425078918021]

    polygon_geom = Polygon(zip(lon_point_list, lat_point_list))
    
    crs = {'init': 'epsg:4326'}
    
    polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])       

    polygon.to_file(filename='polygon_loc2.shp', driver="ESRI Shapefile")


# In[72]:


def location3shp():
    
    lon_point_list = [78.66571158170699, 78.6662346124649, 78.6662346124649, 78.66571158170699, 78.66571158170699]
    lat_point_list = [17.66869116558751, 17.6686911655875, 17.66929686130703, 17.66929686130703, 17.66869116558751]

    polygon_geom = Polygon(zip(lon_point_list, lat_point_list))
    
    crs = {'init': 'epsg:4326'}
    
    polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])       

    polygon.to_file(filename='polygon_loc3.shp', driver="ESRI Shapefile")


# In[ ]:


location1shp() # Run Function
location2shp()
location3shp()


# In[ ]:


msavi2()


# In[91]:


def clip_raster():
    
    args = ['gdalwarp', '-cutline', 'polygon_loc1.shp', '-crop_to_cutline', '-dstalpha', 'msaviImage.tiff', 'clipped.tiff'  ]
    subprocess.Popen(args)


# In[92]:


clip_raster()


# In[ ]:





# In[51]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




