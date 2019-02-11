# Code to use in the calculate window
'Assumed wattage. ' + (!SurvComments! if !SurvComments! else '') 


# Code to use when writing python outside arcpy
import arcpy
arcpy.env.workspace = r"C:\Users\ekitteridge\Desktop" Not Necessary When Run in the ArcPy Window


!FieldName!.strip()

# Caluclate Fields
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' road','Rd')", "PYTHON_9.3")
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' Road','Rd')", "PYTHON_9.3")
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' Manor','Mnr')", "PYTHON_9.3")
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' Trail','Trl')", "PYTHON_9.3")
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' street','St')", "PYTHON_9.3")
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' Street','St')", "PYTHON_9.3")
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' Drive','Dr')", "PYTHON_9.3")
arcpy.CalculateField_management("Norwalk_CT_20181109", "StreetName", r"!StreetName!.replace(' Lane','Ln')", "PYTHON_9.3")


# Selecting by Attribute
arcpy.SelectLayerByAttribute_management("Peterborough_ON_P0009", "NEW_SELECTION", " [RTE_ID] = '2' ")
arcpy.SelectLayerByAttribute_management("Peterborough_ON_P0009", "NEW_SELECTION", ' "RTE_ID" IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 115, 116, 117, 127, 128, 129, 130, 131, 132, 133, 134, 137, 138, 139, 140, 141, 142, 143, 163, 164, 165, 166, 167)')
arcpy.SelectLayerByAttribute_management("Peterborough_ON_P0009", "NEW_SELECTION", ' "SymbolID" IS NULL')
query = "SecondaryConnectionRefresh IS NOT NULL"
arcpy.SelectLayerByAttribute_management("Pittsfield_MA_20180103", "NEW_SELECTION", query)


#Create strip map polygons
	import arcpy
... from arcpy import env
... 
... # Set environment settings
... arcpy.env.workspace = r"C:\Users\Ellen.Ketteridge\Documents\Scratch\20170523_HS2CommunityBoundaries\20170627_CreatedAreasMapSeries\MapSeries.gdb"
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




arcpy.SelectLayerByAttribute_management("Minto_LED_Replacement_14Apr", "NEW_SELECTION", ' "SerialNumb IN" ('SL000626', 'SL000605', 'SL000592', 'SL000596', 'SL000585', 'SL000543'))')


cal2 = arcpy.SelectLayerByAttribute_management("Oxford_ME_20180911", "NEW_SELECTION", ' "RTE_ID" IN (54,79,80)') 
arcpy.CalculateField_management (cal2, "LuminaireType", "\"Sentinel\"", "PYTHON")


cal8 = arcpy.SelectLayerByAttribute_management("Freeport_ME_P0699_Survey", "NEW_SELECTION", ' "RTE_ID" IN (1, 261, 170, 249, 250, 260, 275, 100)') 
arcpy.CalculateField_management (cal8, "InstallCode", "None", "PYTHON")

cal4 = arcpy.SelectLayerByAttribute_management("Freeport_ME_P0699_Survey", "NEW_SELECTION", ' " LEDDesigned = '115W_ATBM-E-MVOLT-R3-3K-MP-NL-P7' ") 
arcpy.CalculateField_management (cal4, "InstallCode", "\"C8\"", "PYTHON")


cal1 = arcpy.SelectLayerByAttribute_management("Freeport_ME_P0699_Survey", "NEW_SELECTION", ' " LEDDesigned = '144W_ESL2-P35S-30K-AS-BK-SG-3-S-P7E-DS-NL2X2-WLDF13-200-BK-P7' ") 
arcpy.CalculateField_management (cal1, "InstallCode", "\"C9\"", "PYTHON")


cal3 = arcpy.SelectLayerByAttribute_management("Freeport_ME_P0699_Survey", "NEW_SELECTION", ' " LEDDesigned = '118W_ESL2-P30S-30K-AS-BK-SG-3-S-P7E-DS-NL2X2-WLDF13-200-BK-P7' ") 
arcpy.CalculateField_management (cal3, "InstallCode", "\"C10\"", "PYTHON")

115W_ATBM-E-MVOLT-R3-3K-MP-NL-P7

arcpy.CalculateField_management("Freeport_ME_P0699_Survey", "LuminaireType", "Sentinel")

arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "NEW_SELECTION", " LEDDesigned = 'No replacement' ")
arcpy.CalculateField_management("Tyngsborough_MA_20180322", "Installation", "No replacement")


cal = arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "NEW_SELECTION", " LEDDesigned = 'No replacement' ")
arcpy.CalculateField_management (cal, "Installation", "\"No replacement\"", "PYTHON")
cal2 = arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "NEW_SELECTION", " LEDDesigned <> 'No replacement' ")
arcpy.CalculateField_management (cal2, "Installation", "\"Pending\"", "PYTHON")

arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "SWITCH_SELECTION")


cal = arcpy.SelectLayerByAttribute_management("Norton_MA_20190129_AuditReconciliation", "NEW_SELECTION", " UMatch = 'Utility Only' ")
arcpy.CalculateField_management (cal, "ProjectNo", "\"\"", "PYTHON")
cal2 = arcpy.SelectLayerByAttribute_management("Tyngsborough_MA_20180322", "NEW_SELECTION", " LEDDesigned <> 'No replacement' ")
arcpy.CalculateField_management (cal2, "Installation", "\"Pending\"", "PYTHON")