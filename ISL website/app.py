from flask import Flask, render_template, request,Response
from PIL import Image
import cv2
import os
import tensorflow as tf
import Detect
#ffe4d1
#ffeee0

lst = ['1', '2', '3', '4','5', '6', '7', '8','9','A', 'B', 'C', 'D','E', 'F', 'G', 'H','I', 'J', 'K', 'L','M', 'N', 'O', 'P','Q','R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
threshold=0.1
nm="centernet"

vid_detector = Detect.Detect()
vid_detector.class_color(lst)
vid_detector.load_model(nm)

app = Flask(__name__)

@app.route('/')
def index():
    if os.path.exists('static/save_img'):
        for i in os.listdir('static/save_img'):
            os.remove('static/save_img/'+i)
    if os.path.exists('static/upload_img'):
        for i in os.listdir('static/upload_img'):
            os.remove('static/upload_img/'+i)
    return render_template('main.html')

@app.route('/detect', methods=['GET','POST'])
def detect():
    # # Get the uploaded image file
    image = request.files['imgfile']

    # # Save the image file to disk
    image_path = 'static/upload_img/'+image.filename
    image.save(image_path)

    a = vid_detector.predictImg(image.filename,lst,threshold)
    filepath = "static/save_img/"+image.filename

    return render_template('Detect.html', filepath=filepath, filename=image.filename)

@app.route('/realtime', methods=['GET','POST'])
def real_time():
    return render_template('real_time.html')


def gen(video):
    while True:
        success, image = video.read()
        img = vid_detector.createBbox(image,lst,threshold)
        ret, jpeg = cv2.imencode('.jpg', img)
        
        frame = jpeg.tobytes()
        
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

            
@app.route('/video_feed')
def video_fd():
    # Set to global because we refer the video variable on global scope, 
    # Or in other words outside the function
    video = cv2.VideoCapture(0)
    # Return the result on the web
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    video.release()

if __name__ == '__main__':
    app.run(debug=True)
