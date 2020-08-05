# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:24:45 2020

@author: skillion
"""

"""2-10 and 2-24 are not full days
2-10 is 6 hours and spans index 33-38
2-24 is 18 hours  """

import arcpy

#set workspace 
arcpy.env.workspace = r'D:\GEOVIIRS\mexico\JS\GEOVIIRS_Mex.gdb'
inTable = "Oaxaca_Fishnet_pop_area_DNB_skyhook_null"


fields = ("*")

fieldName = 'Daily_Point_Count_02_10'
arcpy.AddField_management(inTable, fieldName, "LONG")


with arcpy.da.UpdateCursor(inTable, fields) as cursor:
    for row in cursor:
        total = 0
        for i in range(33, 39):
            if row[i] is not None:
                total += row[i]
        row[len(row)-1] = total
        cursor.updateRow(row)
        
date = 11
i = 39

while (date != 24):
    e = i + 24
    fieldName = 'Daily_Point_Count_02_' + str(date)
    arcpy.AddField_management(inTable, fieldName, "LONG")
    with arcpy.da.UpdateCursor(inTable, fields) as cursor:
        for row in cursor:
            total = 0
            for i in range(i, e):
                if row[i] is not None:
                    total += row[i]
            row[len(row)-1] = total
            cursor.updateRow(row)
        i = e
        date += 1
        

        
        
fieldName = 'Daily_Point_Count_02_24'
arcpy.AddField_management(inTable, fieldName, "LONG")

with arcpy.da.UpdateCursor(inTable, fields) as cursor:
    for row in cursor:
        total = 0
        for i in range(351, 351 + 18):
            if row[i] is not None:
                total += row[i]
        row[len(row)-1] = total
        cursor.updateRow(row)
            
        