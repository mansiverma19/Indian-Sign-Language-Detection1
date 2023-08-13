import pandas as pd
import json
import os
import glob

path="C:\\Users\\mansi\\VS Code Program\\Object detection\\TfodCourse\\ISL\\workspace\\test"
lst=os.listdir(path)
x=0
cnt=0
# for i in lst:
for i in glob.glob(path + '\\*.json'):
    name=i
    # if "-M_front" in name:
    #     clss=name[0] 
    # else:
    #     clss=name.split(".")[0][-1]
    x+=1
    
    file_path=os.path.join(i)

    a_file = open(file_path, "r")
    json_object = json.load(a_file)
    a_file.close()
    # print("#",x,"------->",json_object["predictions"][0]["class"],"-------->",i)
    nm=name.split('\\')[-1]
    # nm=nm.split('.')[0]
    # if len(nm)==1:
    # print(nm)
    # print("----",nm,"----",name)
    try:
        # json_object["predictions"][0]["class"]="6"
        nm=json_object["predictions"][0]["image_path"]
        
        if "json" in nm:
            # print("----",json_object["predictions"][0]["image_path"])
            # nm=nm.replace("S:",r"C:\Users\mansi\VS Code Program")
            nm=nm.replace("json","jpg")
            # print(nm)
            # C:\Users\mansi\VS Code Program\Object detection\TfodCourse\ISL\workspace\train
            json_object["predictions"][0]["image_path"]=str(nm)
            cnt+=1
    except KeyError:
        print("exception")
        # clss=json_object["predictions"]["class"]
        # json_object["predictions"]["class"]="6"
        # dict={
        #     "x": 67.5,
        #     "y": 58.5,
        #     "width": 95.0,
        #     "height": 113.0,
        #     "confidence": 0.8190371990203857,
        #     "class": str(clss),
        #     "image_path": os.path.join("S:\\object detection\\TFODCourse\\ISL\\workspace\\train",i),
        #     "prediction_type": "ObjectDetectionModel"
        # }
        # json_object["predictions"]=[json_object["predictions"]]
    
    a_file = open(file_path, "w")
    json.dump(json_object, a_file,indent=4)
    a_file.close()
print(x,"  ",cnt)
