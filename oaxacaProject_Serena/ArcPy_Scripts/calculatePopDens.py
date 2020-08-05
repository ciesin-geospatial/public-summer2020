# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:30:39 2020

@author: skillion
"""

# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = r'D:\GEOVIIRS\mexico\JS\GEOVIIRS_MEX.gdb'
 
#Oaxaca_Fishnet_pop_area_DNB_skyhook_null
#Oaxaca_Fishnet_pop_area_DNB_skyhook_0
# Set local variables
inTable = "Oaxaca_Fishnet_pop_area_DNB_skyhook_null"
expression = "getPopDens(!GPW_area!, !landscan_2018_pop!)"


#Population Density = Number of People/Land Area
codeblock = """
def getPopDens(area, popCount):
    if area == 0 or area is None or popCount is None:
        return 0
    else:
        return popCount/area"""

#create new field to add counts to          
fieldName = 'popDens'
arcpy.AddField_management(inTable, fieldName, "LONG")

 
# Execute CalculateField 
arcpy.management.CalculateField(inTable, fieldName, expression, "PYTHON3", codeblock)
