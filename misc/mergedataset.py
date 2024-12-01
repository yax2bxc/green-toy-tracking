import datumaro as dm

dataset1 = dm.Dataset.import_from(r"C:\Users\amogus\Desktop\tdata\smiskiseries1", "yolo")
# dataset2 = 
def getDataset(*args):
    mylist = []
    for i in args:
        mystring = r"C:\Users\amogus\Desktop\tdata" + f"\{i}"
        # print(mystring)
        data = dm.Dataset.import_from(mystring, "yolo")
        mylist.append(data)
    return mylist

datasets = getDataset("smiskiseries1","smiskiseries2","smiskiseries3","smiskiseries4")
combination = dm.Dataset.from_extractors(*datasets,merge_policy='intersect')
# print(combination.infos)
combination.export('merged/smiski_all','yolo_ultralytics',save_media=True)