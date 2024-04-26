import numpy as np

# Get the lat,lon
lat = np.load('./input/lat.npy')
lon = np.load('./input/lon.npy')

ny,nx=lat.shape

#change degrees to radians
rad_factor=np.pi/180.0

latvals=lat[:]*rad_factor
lonvals=lon[:]*rad_factor

def grid_id(lat_in,lon_in): 
    usr_latval=lat_in*rad_factor
    usr_lonval=lon_in*rad_factor
    clat,clon = np.cos(latvals), np.cos(lonvals)
    slat,slon = np.sin(latvals), np.sin(lonvals)
    delX = np.cos(usr_latval)*np.cos(usr_lonval) - clat*clon
    delY = np.cos(usr_latval)*np.sin(usr_lonval) - clat*slon
    delZ = np.sin(usr_latval) - slat;
    dist_sq = delX**2 + delY**2 + delZ**2
    minindex_1d = dist_sq.argmin()
    iy_min, ix_min = np.unravel_index(minindex_1d, latvals.shape)
    return (ix_min, 240-iy_min)