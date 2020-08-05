# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:09:18 2020

@author: skillion
"""

import arcpy

arcpy.CheckOutExtension("Spatial")
# Define input workspace and create list of rasters
arcpy.env.workspace = r'D:\GEOVIIRS\mexico\2018\raw\h08v07'

rasters = arcpy.ListRasters()


# Run cell statistics to calculate mean
3calc = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
calc.save(r'D:\GEOVIIRS\mexico\2018\raw\2018_mean')

arcpy.env.workspace = r'D:\GEOVIIRS\mexico\JS\GEOVIIRS_Mex.gdb'
inFeature = "Oaxaca_Fishnet_pop_area_DNB_skyhook_0"
table = r"D:\GEOVIIRS\mexico\JS\GEOVIIRS_Mex.gdb\Oaxaca_2018_NTL_Avg"

#convert raster to table
arcpy.sa.ZonalStatisticsAsTable(inFeature, "gridcode", r"D:\GEOVIIRS\mexico\2018\raw\2018_mean", table, "DATA", "ALL", "CURRENT_SLICE")

#join field to inFeature
arcpy.JoinField_management(inFeature, "gridcode", table, "gridcode", 
                           ["MAX"])

