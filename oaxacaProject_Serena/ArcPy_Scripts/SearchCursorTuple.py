import csv
sr = arcpy.SpatialReference(4326)
with open(r'D:\GEOVIIRS\mexico\JS\tables\J_Skyhook_Tuple.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in arcpy.da.SearchCursor('skyhook_2018_2_11_to_2018_2_24_raw_spjoin_dissolve', '*', None, sr, True):
        spamwriter.writerow(row)
print('done')
