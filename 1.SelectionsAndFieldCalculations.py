###
# Selecting By Attribute, Create selections as one would normally use in the GUI, 'Select By Attribute'
###

# Documentation: http://pro.arcgis.com/en/pro-app/tool-reference/data-management/select-layer-by-attribute.htm

# Examples:
# SelectLayerByAttribute_management(in_layer_or_view, {selection_type}, {SQL_where_clause}, {invert_where_clause})
arcpy.SelectLayerByAttribute_management("PointFC", "NEW_SELECTION", "Fruit IN ( 'Apples' , 'Kiwis' )")
arcpy.SelectLayerByAttribute_management("PointFC", "NEW_SELECTION", "TestID IN (1, 2, 3, 4, 5)")
arcpy.SelectLayerByAttribute_management("PointFC", "SUBSET_SELECTION", "FreeText IS NULL")
arcpy.SelectLayerByAttribute_management("PointFC", "SUBSET_SELECTION", "FreeText IS NOT NULL")
arcpy.SelectLayerByAttribute_management("PointFC", "ADD_TO_SELECTION", "Fruit <> 'Bananas'")
arcpy.SelectLayerByAttribute_management("PointFC", "ADD_TO_SELECTION", "Fruit LIKE 'Bananas'")
arcpy.SelectLayerByAttribute_management("PointFC", "ADD_TO_SELECTION", "Fruit = 'Kiwis'")
arcpy.SelectLayerByAttribute_management("PointFC", "SWITCH_SELECTION")
arcpy.SelectLayerByAttribute_management("PointFC", "CLEAR_SELECTION")


#############################################################################################################################

###
# Calculate Field, Create calculations as one would normally use in the GUI 'Calculate Field' on the attribute table.
###

# Documentation: http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field.htm

# Examples:
# CalculateField_management (in_table, field, expression, {expression_type}, {code_block})
arcpy.CalculateField_management("PointFC", "TestCalcs", "\"Oranges\"", "PYTHON_9.3")
arcpy.CalculateField_management("PointFC", "Fruit", r"!Fruit!.replace('Kiwis','Oranges')", "PYTHON_9.3")
arcpy.CalculateField_management("PointFC", "Vegetable", r"!Vegetable!.title()", "PYTHON_9.3")
arcpy.CalculateField_management("PointFC", "Vegetable", r"!Vegetable!.strip()", "PYTHON_9.3")
arcpy.CalculateField_management("PointFC", "TestCalcs", r"TestID * 100", "PYTHON_9.3")


#############################################################################################################################

###
# Combining Select and Calculate Field with Variable , Select a range of values by their ID and update their value in the fruit field to 'Mangoes'.
###


select = arcpy.SelectLayerByAttribute_management("PointFC", "NEW_SELECTION", "TestID IN (6, 7, 8, 9, 10)")
arcpy.CalculateField_management(select, "Fruit", "\"Mangoes\"", "PYTHON_9.3")


#############################################################################################################################

###
# Creating Another Variable, Select a range of values by their ID and update their value in the fruit field to 'Pears'.
###

inputFeatureClass = "PointFC"

select = arcpy.SelectLayerByAttribute_management(inputFeatureClass, "NEW_SELECTION", "TestID IN (1, 2, 3, 4, 5)")
arcpy.CalculateField_management(select, "Fruit", "\"Pears\"", "PYTHON_9.3")


#############################################################################################################################

###
# Creating Two Variables, Select a range of values by their ID and update their value in the fruit field to 'Mandarins'.
###

inputFeatureClass = "PointFC"
query = "TestID IN (11, 12, 13, 14, 15)"

select = arcpy.SelectLayerByAttribute_management(inputFeatureClass, "NEW_SELECTION", query)
arcpy.CalculateField_management(select, "Fruit", "\"Mandarins\"", "PYTHON_9.3")


#############################################################################################################################

###
# No Hardcoding, Select all values in vegetable field with value 'Pumpkins' and change to 'Asparagus'.
###

inputFeatureClass = "PointFC"
fieldName = "Vegetable"
query = fieldName + " = 'Pumpkins'"
newValue = "\"Asparagus\""
selectionType = "NEW_SELECTION"

print (query)
# It is good practice to print any variables that involved a calculation, this will help with troubleshooting.

select = arcpy.SelectLayerByAttribute_management(inputFeatureClass, selectionType, query)
arcpy.CalculateField_management(select, fieldName, newValue, "PYTHON_9.3")


#############################################################################################################################