    ## How to List All Unique Values for a Field in A Table

table = "Cityname_SP_YYYYMMDD"
field = "NameOfField"

with arcpy.da.SearchCursor(table, [field]) as cursor:
    myValues = sorted({row[0] for row in cursor})

print (myValues)

    ## How to List All Fields in A Table
featureclass = "Cityname_SP_YYYYMMDD"
fieldNames = [f.name for f in arcpy.ListFields(featureclass)]
print (fieldNames)


    ## How to List Feature Classes in a f.Gdb
arcpy.env.workspace = "C:/RTE/Municipality/Cityname_SP/Cityname_SP.gdb"
featureclasses = arcpy.ListFeatureClasses()
print (featureclasses)



field = "LEDDesigned"
field2 = "LuminaireType"
with arcpy.da.SearchCursor(InputFeatureClass, [field, field2]) as cursor:
   for row in cursor:
        print(row)


featureClass = "Cityname_SP_YYYYMMDD"
field = "LuminaireType"
cursor = arcpy.SearchCursor(featureClass)
for row in cursor:
    print(row.getValue(field))



#Sort Fields Multiple
rows = arcpy.SearchCursor("Cityname_SP_YYYYMMDD",
                          fields="LuminaireType; LEDDesigned",
                          sort_fields="LuminaireType A; LEDDesigned A")
for row in rows:
    print("{0}, {1}".format(
        row.getValue("LuminaireType"),
        row.getValue("LEDDesigned")))

    
#Sort Fields Single
rows = arcpy.SearchCursor("Cityname_SP_YYYYMMDD",
                          fields="LEDDesigned",
                          sort_fields="LEDDesigned A")
for row in rows:
    print("{0}".format(
        row.getValue("LEDDesigned")))