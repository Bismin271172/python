import processing

#input = 'F:/kb-cmip6/input/csv/'
#output='F:/kb-cmip6/output/csv/'
input='/media/kboonma/kbtoshi/kb-cmip6/input/shp/'
output='/media/kboonma/kbtoshi/kb-cmip6/output/lsf_fac/'
var_list = ['pr_','tasmin_','tasmax_']

for var in var_list:
    for i1 in range (0,12):
        processing.run("qgis:idwinterpolation",\
        {'INTERPOLATION_DATA':input+str(var)+'fac.shp::~::0::~::'+str(i1+3)+'::~::0',\
        'DISTANCE_COEFFICIENT':3,\
        'EXTENT':'88.00000 ,98.00000,23.00000, 29.00000 [EPSG:4326]',\
        'PIXEL_SIZE':0.045,\
        'OUTPUT':output+str(var)+'factor_'+str(i1+1)+'.tif'})
