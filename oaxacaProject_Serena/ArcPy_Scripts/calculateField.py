# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:30:39 2020

@author: skillion
"""

# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = r'D:\GEOVIIRS\mexico\JS\GEOVIIRS_MEX.gdb'
 
# Set local variables
inTable = "skyhook_2018_2_11_to_2018_2_24_raw_spjoin_dissolve"
fieldName = "DoM_HoD_"
var = "FIRST_FIRST_day_of_month"
var2 = "FIRST_FIRST_hour_of_day"
expression = "getDateHour(!FIRST_FIRST_day_of_month!, !FIRST_FIRST_hour_of_day!)"

codeblock = """
def getDateHour(d, h):
    d = str(d)
    h = str(h)
    result = ''
    if len(h) < 2:
        result = d + '_' + '0' + h
    else:
        result = d + '_' + h
    return result"""
        

 
# Execute CalculateField 
arcpy.management.CalculateField(inTable, fieldName, expression, "PYTHON3", codeblock)
