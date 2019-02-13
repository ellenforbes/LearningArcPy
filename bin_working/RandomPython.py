
#adding assumed wattage
# Code to use in the calculate window
'Assumed wattage. ' + (!SurvComments! if !SurvComments! else '') 



#Create strip map polygons
	import arcpy
... from arcpy import env
... 
... # Set environment settings
... arcpy.env.workspace = r"C:\Users\Ellen.Ketteridge\Documents\Scratch\MapSeries.gdb"
... 
... # Set local variables
... inFeatures = "Manchester"
... outFeatureClass = "MapSeriesManchester"
... lenA = "4 Kilometers"
... lenP = "2.5 Kilometers"
... 
... # Execute StripMapIndexFeatures
... arcpy.StripMapIndexFeatures_cartography (inFeatures, outFeatureClass, "",
...                                          "", lenA, lenP)


#Calculating no replacements
cal = arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "NEW_SELECTION", " LEDDesigned = 'No replacement' ")
arcpy.CalculateField_management (cal, "Installation", "\"No replacement\"", "PYTHON")
cal2 = arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "NEW_SELECTION", " LEDDesigned <> 'No replacement' ")
arcpy.CalculateField_management (cal2, "Installation", "\"Pending\"", "PYTHON")

arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "SWITCH_SELECTION")



# PIR
arcpy.SelectLayerByAttribute_management("Pittsfield_MA_20180103", "NEW_SELECTION", " Installation = 'Installed' ")
query = "InstlDate > date '2019-01-11 00:01:01' AND InstlDate < date '2019-01-23 23:59:59'"
arcpy.SelectLayerByAttribute_management("Pittsfield_MA_20180103", "SUBSET_SELECTION", query)
