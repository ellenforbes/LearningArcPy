#1 Code to use in the Calculate Window for Assumed Wattage
	'Assumed wattage. ' + (!SurvComments! if !SurvComments! else '') 

#2 Replace Text using Caluclate Fields
	arcpy.CalculateField_management("Cityname_SP_20180101", "FieldName", r"!FieldName!.replace('originaltext','replacementtext')", "PYTHON_9.3")


#3 Selecting by Attribute
	arcpy.SelectLayerByAttribute_management("Cityname_SP_20180101", "NEW_SELECTION", " FieldName = 'StringValue' ")
	arcpy.SelectLayerByAttribute_management("Cityname_SP_20180101", "NEW_SELECTION", " FieldName = 1 ")
	arcpy.SelectLayerByAttribute_management("Cityname_SP_20180101", "NEW_SELECTION", ' "FieldName" IN (1, 2, 3, 4, 5, 6)')
	arcpy.SelectLayerByAttribute_management("Cityname_SP_20180101", "NEW_SELECTION", ' "FieldName" IS NULL')
	arcpy.SelectLayerByAttribute_management("Cityname_SP_20180101", "SUBSET_SELECTION", " FieldName = 'StringValue' ")


#4 Selecting by Attribute with Separated Query
	query = "LampWattage IS NULL"
	arcpy.SelectLayerByAttribute_management("Cityname_SP_20180101", "NEW_SELECTION", query)

Pittsfield PIR
arcpy.SelectLayerByAttribute_management("Pittsfield_MA_20180103", "NEW_SELECTION", " Installation = 'Installed' ")
query = "InstlDate > date '2019-01-11 00:01:01' AND InstlDate < date '2019-01-23 23:59:59'"
arcpy.SelectLayerByAttribute_management("Pittsfield_MA_20180103", "SUBSET_SELECTION", query)
