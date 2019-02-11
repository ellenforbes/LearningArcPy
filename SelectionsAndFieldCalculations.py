###
# Selecting By Attribute
###

# Documentation: http://pro.arcgis.com/en/pro-app/tool-reference/data-management/select-layer-by-attribute.htm

# Examples:
# SelectLayerByAttribute_management(in_layer_or_view, {selection_type}, {SQL_where_clause}, {invert_where_clause})
arcpy.SelectLayerByAttribute_management("Cityname_SP_YYYYMMDD", "NEW_SELECTION", ' "FieldName" IN (1, 2, 3, 4, 5)')
arcpy.SelectLayerByAttribute_management("Cityname_SP_YYYYMMDD", "SUBSET_SELECTION", '"FieldName" IS NULL')
arcpy.SelectLayerByAttribute_management("Cityname_SP_YYYYMMDD", "REMOVE_FROM_SELECTION", '"FieldName" IS NOT NULL')
arcpy.SelectLayerByAttribute_management("Cityname_SP_YYYYMMDD", "ADD_TO_SELECTION", 'FieldName <> "No replacement"')
arcpy.SelectLayerByAttribute_management("Cityname_SP_YYYYMMDD", "SWITCH_SELECTION")
arcpy.SelectLayerByAttribute_management("Cityname_SP_YYYYMMDD", "CLEAR_SELECTION")


#############################################################################################################################

###
# Calculate Field
###

# Documentation: http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field.htm

# Examples:
# CalculateField_management (in_table, field, expression, {expression_type}, {code_block})
arcpy.CalculateField_management("Cityname_SP_YYYYMMDD", "FieldName", "\"ReplacementValue\"", "PYTHON_9.3")
arcpy.CalculateField_management("Cityname_SP_YYYYMMDD", "FieldName", r"!FieldName!.replace('old value','new value')", "PYTHON_9.3")
arcpy.CalculateField_management("Cityname_SP_YYYYMMDD", "FieldName", r"!FieldName!.title()", "PYTHON_9.3")
arcpy.CalculateField_management("Cityname_SP_YYYYMMDD", "FieldName", r"!FieldName!.strip()", "PYTHON_9.3")
arcpy.CalculateField_management("Cityname_SP_YYYYMMDD", "FieldName", "FieldName * 100", "SQL")


#############################################################################################################################

###
# Combining Select and Calculate Field with Variable
###


select = arcpy.SelectLayerByAttribute_management("Cityname_SP_YYYYMMDD", "NEW_SELECTION", ' "FieldName" IN (1, 2, 3, 4, 5)')
arcpy.CalculateField_management(select, "FieldName", "\"ReplacementValue\"", "PYTHON_9.3")


#############################################################################################################################

###
# Creating Another Variable
###

inputFeatureClass = "Cityname_SP_YYYYMMDD"

select = arcpy.SelectLayerByAttribute_management(inputFeatureClass, "NEW_SELECTION", ' "FieldName" IN (1, 2, 3, 4, 5)')
arcpy.CalculateField_management(select, "FieldName", "\"ReplacementValue\"", "PYTHON_9.3")


#############################################################################################################################

###
# Creating Two Variables
###

inputFeatureClass = "Cityname_SP_YYYYMMDD"
query = ' "FieldName" IN (1, 2, 3, 4, 5)'

select = arcpy.SelectLayerByAttribute_management(inputFeatureClass, "NEW_SELECTION", query)
arcpy.CalculateField_management(select, "FieldName", "\"ReplacementValue\"", "PYTHON_9.3")


#############################################################################################################################

###
# No Hardcoding
###

inputFeatureClass = "Cityname_SP_YYYYMMDD"
fieldName = "RTE"
query = fieldName + " = No replacement"
newValue = "\"ReplacementValue\""
selectionType = "NEW_SELECTION"

select = arcpy.SelectLayerByAttribute_management(inputFeatureClass, selectionType, query)
arcpy.CalculateField_management(select, fieldName, newValue, "PYTHON_9.3")