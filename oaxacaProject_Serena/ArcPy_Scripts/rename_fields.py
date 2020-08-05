# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:39:59 2020

@author: skillion
"""

#convert shapefile to geodatabase table to rename fields
feature = r'D:\GEOVIIRS\mexico\skyhook\bounding_geometry\fishnetLayer_joined.shp'
arcpy.env.workspace = r'D:\GEOVIIRS\mexico\JS\data\fishnet_joined.gdb'
arcpy.CreateFileGDB_management(r'D:\GEOVIIRS\mexico\JS\data', "fishnet_joined.gdb")
arcpy.FeatureClassToGeodatabase_conversion(feature, "fishnet_joined.gdb")


#list all fields
fieldList = arcpy.ListFields( r'D:\GEOVIIRS\mexico\JS\data\fishnet_joined.gdb\fishnetLayer_joined')


#routine to rename starting at index 4 to 32
i = 1
d = 11
for field in range(4,32):
    if i % 2 == 0:
        band = 2
    else:
        band = 1
    name = 'b' + str(band) + '_' + '02' + str(d)    
    alias = 'band' + str(band) + '_' + '02' + '_' + str(d)
    arcpy.AlterField_management("fishnetLayer_joined", fieldList[field].name, name, alias)
    i += 1
    if band == 2:
        d += 1
    print(name)