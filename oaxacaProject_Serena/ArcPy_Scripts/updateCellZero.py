# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:05:20 2020

@author: skillion
"""

import arcpy

#set workspace 
arcpy.env.workspace = r'D:\GEOVIIRS\mexico\JS\GEOVIIRS_Mex.gdb'
inTable = "Oaxaca_Fishnet_pop_area_DNB_skyhook_0"




fields = ("*")



#iterate each row and update field, field index 33 to 369
with arcpy.da.UpdateCursor(inTable, fields) as cursor:
    for row in cursor:
        for i in range (33, 369):
            if row[i] is None:
                row[i] = 0
                cursor.updateRow(row)


  
