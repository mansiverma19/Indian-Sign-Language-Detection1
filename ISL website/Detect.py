import cv2
import time, os
import tensorflow as tf
import numpy as np
# from tensorflow.python.kreras.utils.data_utils import get_file

np.random.seed(123)

class Detect:
    def __init__(self):
        pass

    def class_color(self, classlst):
        n = len(classlst)
        self.colorlst = np.random.uniform(low=0, high=255, size=(n,3))
        # print(len(self.colorlst), n)

    def load_model(self, model_name):
        # print(model_name)
        tf.keras.backend.clear_session()
        self.model = tf.saved_model.load('model\saved_model')
        # print("loaded successfully")

    def createBbox(self, img, classlst, threshold):
        # input_arr = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
        input_arr = np.array(img)
        input_tensor = tf.convert_to_tensor(np.expand_dims(input_arr, 0), dtype=tf.uint8)
        # print("(---------------------------------------------------)")
        # print(input_tensor)
        # print("beforw*****************************************************************************************************")
        detections = self.model(input_tensor)

        bounding_box = detections['detection_boxes'][0].numpy()
        classIndexs = detections['detection_classes'][0].numpy().astype(np.int32)
        classScore = detections['detection_scores'][0].numpy()
        img_h, img_w, img_c = img.shape
        bbox_indx = tf.image.non_max_suppression(bounding_box, classScore, max_output_size=50, iou_threshold=0.5, score_threshold=threshold)
        # print('bbox',bounding_box)
        # print('score',classScore)     
        if len(bbox_indx)!=0:
            for i in bbox_indx:
                bbox = tuple(bounding_box[i].tolist())
                classConfidence = round(100*classScore[i])
                classIndex = classIndexs[i]
                classLabel = classlst[classIndex]
                classColor = self.colorlst[classIndex]

                display = '{} : {}%'.format(classLabel, classConfidence)

                y_min, x_min, y_max, x_max = bbox

                # tup = (x_min,y_min,x_max,y_max,classLabel, classConfidence)

                x_min, y_min, x_max, y_max = (x_min*img_w, y_min*img_h, x_max*img_w, y_max*img_h)
                x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)

                cv2.rectangle(img, (x_min,y_min), (x_max,y_max), color=classColor, thickness=1)
                cv2.putText(img, display, (x_min,y_min-10), cv2.FONT_HERSHEY_COMPLEX, 1,classColor, 2)

                line_wdth = min(int((x_max-x_min)*0.2), int((y_max-y_min)*0.2),)
                cv2.line(img, (x_min, y_min), (x_min+line_wdth, y_min), classColor, thickness=3)
                cv2.line(img, (x_min, y_min), (x_min, y_min+line_wdth), classColor, thickness=3)

                cv2.line(img, (x_min, y_max), (x_min+line_wdth, y_max), classColor, thickness=3)
                cv2.line(img, (x_min, y_max), (x_min, y_max-line_wdth), classColor, thickness=3)

                cv2.line(img, (x_max, y_min), (x_max-line_wdth, y_min), classColor, thickness=3)
                cv2.line(img, (x_max, y_min), (x_max, y_min+line_wdth), classColor, thickness=3)

                cv2.line(img, (x_max, y_max), (x_max-line_wdth, y_max), classColor, thickness=3)
                cv2.line(img, (x_max, y_max), (x_max, y_max-line_wdth), classColor, thickness=3)
        return img      

    def predictImg(self, filename, classlst, threshold): 
        # print("imread----------------------------------------------------------------------------------")
        # img = cv2.imread('static/upload_img/'+filename)
        pth="static/site_img/"+filename
        print(filename)
        img = cv2.imread(pth)
        bboxImg = self.createBbox(img, classlst, threshold)
        # print("----------------------------------------------------------------------------------")
        save = cv2.imwrite('static/save_img/'+filename,bboxImg)
        print("image saved :",save)

        return bboxImg
