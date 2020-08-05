# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:05:20 2020

@author: skillion
"""

import arcpy

#set workspace 
arcpy.env.workspace = r'D:\GEOVIIRS\mexico\JS\GEOVIIRS_Mex.gdb'
inTable = "skyhook_2018_2_11_to_2018_2_24_raw_spjoin_dissolve"

#declare an empty dictionary
gridDict = {}

#iterate through each row, count the number of occurences for gridcode_DD_HH
for row in arcpy.da.SearchCursor(inTable, '*', None, None, True):
        gridID = row[10] #gridcode_DD_HH
        if gridID in gridDict.keys():
            gridDict[gridID] += 1
        else:
            gridDict[gridID] = 1
            
#create new field to add counts to          
fieldName = 'gridCount_Time'
arcpy.AddField_management(inTable, fieldName, "LONG")

#fields to reference for update 
#i.e updating gridCount_Time with count of gridcode_DD_HH from gridDict
fields =  ['gridcode_DD_HH', 'gridCount_Time']

#iterate each row and update field
with arcpy.da.UpdateCursor(inTable, fields) as cursor:
    for row in cursor:
        row[1] = gridDict[row[0]]
        cursor.updateRow(row)
  
