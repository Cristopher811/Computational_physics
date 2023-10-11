import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from scipy.interpolate import Rbf
 
lats = [38.895,51.165691,55.378051,46.227638,61.52401,36.204824,52.132633,56.130366,41.87194,60.128161,47.516231,46.818188,56.26392,35.86166,31.791702,53.41291,20.593684,30.375321,50.503887,53.709807,47.162494]
lons = [-77.0366,10.451526,-3.435973,2.213749,105.318756,138.252924,5.291266,-106.346771,12.56738,18.643501,14.550072,8.227512,9.501785,104.195397,-7.09262,-8.24389,78.96288,69.345116,4.469936,27.953389,19.503304]
data = [96,28,25,16,11,10,9,5,5,4,4,4,3,2,1,1,1,1,1,1,1]
print(len(lats), len(lons), len(data))
 
# Create a meshgrid for interpolation
xi = np.linspace(-180, 180, 100)
yi = np.linspace(-90, 90, 100)
xi, yi = np.meshgrid(xi, yi)
 
# Different functions for the spherical interpolation:
# 'linear': Linear radial basis function
# 'multiquadric': Multiquadric radial basis function
# 'inverse': Inverse radial basis function
# 'gaussian': Gaussian radial basis function
# 'cubic': Cubic radial basis function
# 'quintic': Quintic radial basis function
# 'thin_plate': Thin-plate spline radial basis function
 
# Perform 2D interpolation using Rbf for spherical interpolation
rbf = Rbf(lons, lats, data, function='linear')
zi = rbf(xi, yi)
 
# Create a Cartopy PlateCarree projection centered at lon = 0
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=0))
 
# Add coastlines and gridlines
ax.coastlines()
ax.gridlines(draw_labels=True)
 
# Set extent of the plot
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
 
# Create color plot
plt.pcolormesh(xi, yi, zi, shading='auto', cmap='viridis')
 
# Create scatter plot with data as color
scatter = ax.scatter(lons, lats, c=data, cmap='viridis', s=100,\
                     edgecolors='black',linewidths=1,\
                     transform=ccrs.PlateCarree())
 
# Add colorbar
cbar = plt.colorbar(scatter, label='Number of physics nobel prize winners by country', ax=ax, shrink=0.7, pad = .1)
cbar.mappable.set_clim(0, 91)
 
# Add title
plt.title('2D Interpolation Colorplot with\nScatter Plot (PlateCarree Projection)')
 
plt.show()
