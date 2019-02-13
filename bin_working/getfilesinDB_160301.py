import arcpy, os, csv

locationDB = r"\\Global.com\london\PTG\05 Internal Project Data\00-1 WIP\01 Data\DataToGoToSDE\REF_ADM.gdb"
locationCSV = r"C:\Users\Ellen.Ketteridge\Desktop\REF_ADM.csv "

fcs = []
def listFcsInGDB(gdb):
    arcpy.env.workspace=gdb
    for fds in arcpy.ListDatasets('','feature') + ['']: #gdb dataset
        for fc in arcpy.ListFeatureClasses('','',fds): #get fc
            fcs.append(os.path.join(fds, fc))
        for tb in arcpy.ListTables(): #get tables
            fcs.append(os.path.join(fds, tb))
        for rt in arcpy.ListRasters():
            fcs.append(os.path.join(fds, rt))
    return fcs

fcs = listFcsInGDB(locationDB)

with open(locationCSV, 'wb') as f:
    w = csv.writer(f)
    w.writerow(["Dataset name", "Imported"])
    for fc in fcs:
        w.writerow([fc])
