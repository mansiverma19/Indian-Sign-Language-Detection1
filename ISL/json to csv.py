import os
import glob
import pandas as pd
import json
import pickle

def json_to_csv():
    path_to_json = 'C:/Users/mansi/VS Code Program/Object detection/TfodCourse/ISL/workspace/train_label'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    path_to_jpeg = 'C:/Users/mansi/VS Code Program/Object detection/TfodCourse/ISL/workspace/train'
    jpeg_files = [pos_jpeg for pos_jpeg in os.listdir(path_to_jpeg) if pos_jpeg.endswith('.jpeg')]
    fjpeg=(list(reversed(jpeg_files)))
    n=0
    csv_list = []
    labels=[]
    for j in json_files:
        data_file=open('C:/Users/mansi/VS Code Program/Object detection/TfodCourse/ISL/workspace/train_label/{}'.format(j))   
        data = json.load(data_file)
        width,height=data['display_width'],data['display_height']
        for item in data["items"]:
            box = item['bounding_box']
            if item['upc']!='None':
                name=item['upc']
                labels.append(name)
                xmin=box['left']
                ymin=box['top']
                xmax=box['right']
                ymax=box['bottom']
                value = (fjpeg[n],
                         width,
                         height,
                         name,
                         xmin,
                         ymin,
                         xmax,
                         ymax
                         )
                csv_list.append(value)
            n=n+1
        
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    csv_df = pd.DataFrame(csv_list, columns=column_name)
    labels_train=list(set(labels))
    with open("train_labels.txt", "wb") as fp:   #Pickling
        pickle.dump(labels_train, fp)
    return csv_df

def main():
    for directory in ['train']:
        csv_df = json_to_csv()
        csv_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted json to csv.')

main()