# <b><h1 align="center">Indian-Sign-Language-Detection</h1></b>
<ul>
<li><h2>Website View of the Indian sign language(ISL) detection</h2></li><br>
    
 https://github.com/mansiverma19/Indian-Sign-Language-Detection1/assets/83285383/61add4dc-aa3b-4691-95f0-29b1bcd8f4a7
   
<li><h2>Mobile View of the Indian sign language(ISL) detection</h2></li><br>
  
https://github.com/mansiverma19/Indian-Sign-Language-Detection1/assets/83285383/0d2aa7f9-a5ed-4631-8efd-6c316b009364
   
</ul>

:file_folder:ISL<br>
    <ul>
    <li>:file_folder:API<br></li>
    <li>:file_folder:PROTOC<br></li>
    <li>:file_folder:scripts<br></li>
         <ul>
            <li>:page_facing_up:json to csv.py</li>
            <li>:page_facing_up:json_generate_tfrecord-1.py</li>
        </ul>
    <li>:file_folder:workspace<br></li>
        <ul>
            <li>:file_folder:image</li>
            <li>:file_folder:labelimg</li>
            <li>:file_folder:labels</li>
                <ul>
                    <li>:page_facing_up:label_map.pbtxt</li>
                    <li>:page_facing_up:test.record</li>
                    <li>:page_facing_up:train.record</li>
                </ul>
            <li>:file_folder:pre-trained-models</li>
                <ul>
                    <li>:file_folder:centernet_resnet50_v2_512x512_coco17_tpu-8</li>
                    <li>:page_facing_up:centernet_resnet50_v2_512x512_coco17_tpu-8.tar.gz</li>
                </ul>
            <li>:file_folder:test</li>
            <li>:file_folder:test_label</li>
            <li>:file_folder:train</li>
            <li>:file_folder:train_label</li>
            <li>:file_folder:validate</li>
            <li>:file_folder:video</li>
            <li>:page_facing_up:label_correction.py</li>
        </ul>
    </ul>
:file_folder:ISL website<br>
    <ul>
    <li>:file_folder:model<br></li>
         <ul>
            <li>:file_folder:checkpoint</li>
            <li>:file_folder:saved_model</li>
            <li>:page_facing_up:pipeline.config</li>
        </ul>
    <li>:file_folder:static<br></li>
        <ul>
            <li>:file_folder:save_img</li>
            <li>:file_folder:site_img</li>
            <li>:file_folder:upload_img</li>
            <li>:page_facing_up:main.css</li>
        </ul>
    <li>:file_folder:templates<br></li>
        <ul>
            <li><img src="ISL website/static/site_img/chrome.png" height=2% width=2%>Detect.html</li>
            <li><img src="ISL website/static/site_img/chrome.png" height=2% width=2%>main.html</li>
            <li><img src="ISL website/static/site_img/chrome.png" height=2% width=2%>real_time.html</li>
            <li><img src="ISL website/static/site_img/chrome.png" height=2% width=2%>carousel.html</li>
        </ul>
    <li>:page_facing_up:app.py<br></li>
    <li>:page_facing_up:Detect.py<br></li>
    <li>:page_facing_up:run.py<br></li>
    <li>:whale:Dockerfile<br></li>
    <li>:page_facing_up:requirements.txt<br</li>
    </ul>
:page_facing_up:indian sign lang model.ipynb<br>
:page_facing_up:indian sign language dataset creation.ipynb<br>

<b><h1>STEPS</h1></b><br>
<ol>
    <h1><li>INSTALLATION</h1></li>
        Link for reference of installation. 
        <ol>
            <h3><li>Create virtual environment and activate it</li></h3>
<pre>
conda create -n tfod1 pip python=3.9
conda activate tfod1</pre>
            <h3><li>TensorFlow Installation</li></h3>
                <a href="https://www.youtube.com/watch?v=dMh7krojLIE&t=0s">Youtube</a>
<pre>
# Install
pip install --ignore-installed --upgrade tensorflow== 2.10.1
# Verify installation
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"</pre>
            <h3><li>GPU Support(optional)</li></h3>
                <a href="https://www.youtube.com/watch?v=H3ycAoGM_Hk&t=0s">Youtube</a>
                <p><b>GPU</b>: NVIDIA GeForce GTX 3050  </p>
                <h4># CUDA Toolkit Installation</h4>
                <a href="https://developer.nvidia.com/cuda-11.2.2-download-archive                target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork">CUDA INSTALL</a> 
<pre>
CUDA Toolkit v11.7 </pre>
                <h4># CUDNN Installation</h4>
                <a href="https://developer.nvidia.com/rdp/cudnn-archive">CuDNN INSTALL</a>
<pre>
CuDNN v8.4.1    </pre>
            <h3><li>Download TensorFlow Model Garden</li></h3>
                <a href="https://www.youtube.com/watch?v=H3ycAoGM_Hk&t=0s">Youtube</a>
                <p>To download the models you can either use Git to clone the <a hhref="https://github.com/tensorflow/models">TensorFlow-Model-Garden</a> repository inside the TensorFlow folder, or you can simply download it as a ZIP and extract its contents</p>
            <h3><li>Protobuf Installation</li></h3>
                <a href="https://www.youtube.com/watch?v=m97aGEhsraM&t=0s">Youtube</a>
                <p>Download the latest protoc-*-*.zip release (e.g. protoc-3.12.3-win64.zip for 64-bit Windows)
Extract the contents of the downloaded protoc-*-*.zip in a directory <PATH_TO_ProtoBuf> (e.g. C:\Program Files\Google Protobuf)</p>
                <p>Add <PATH_TO_ProtoBuf>\bin to your Path environment variable.</p>
<pre>
protoc object_detection/protos/*.proto --python_out=.</pre>
            <h3><li>COCO API and Object Detection API Installation</li></h3>
                <a href="https://www.youtube.com/watch?v=lYu_Wz5Zbhg&list=PLpkFduNMb9uInRPXI-2CtNDq4DYXm9cUK&index=5">Youtube</a>
<pre>
#Coco API
pip install cython
pip install git+https://github.com/philferriere/cocoapi.git
#object detection API
cp object_detection/packages/tf2/setup.py .
python -m pip install .</pre>
                <p>IF error: Microsoft Visual C++ 14.0 or greater is required. <a href="https://www.youtube.com/watch?v=rcI1_e38BWs">Solution</a></p>
            <h3><li>Verify installation</li></h3>
<pre>
python object_detection/builders/model_builder_tf2_test.py</pre>
        </ol>
    <h1><li>DATASET CREATION</h1></li>
        <ol>
            <h3><li>Collecting Images</li></h3>
                <h6>1.From Kaggle :  <a href="https://www.kaggle.com/datasets/vaishnaviasonawane/indian-sign-language-dataset">Dataset link</a></h6>
                <h6>2.Generating Video and Converting each frame as image.<a href="https://github.com/mansiverma19/Indian-Sign-Language-Detection1/blob/main/ISL/indian%20sign%20language%20dataset%20creation.ipynb">Code</a></h6>
            <h3><li>Data Augmentation</li></h3>
                <h4>Library used : <i>Imgaug</i></h4>
                <h4>Features based on which dataset is augmented</h4>
                <ul><li>Fliplr</li>
                    <li>GaussianBlur</li>
                    <li>LinearContrast</li>
                    <li>Multiply</li>
                    <li>Sharpen</li>
                    <li>lightness</li>
                    <li>Invert</li>
                    <li>Crop</li></ul>
            <h3><li>Data Annotation</li></h3>
                <p>The images are annotated using the platform <a href="https://roboflow.com/">RoboFlow</a>.</p>
                <p>It is the platform where user can upload the image data and can annotate multiple objects in an image.</p>
                <p>This platform can be used as tool to auto-annotate the images. Firstly few images can be annoated manually and using that data model is trained and using that model we can auto-annotate multiple images in local machine.</p>
                <h4>Cloning and Virtual environment</h4>
<pre>
# clone repository and navigate to root directory
git clone git@github.com:roboflow-ai/auto-annotate.git
cd auto-annotate
# setup python environment and activate it
python3 -m venv venv
source venv/bin/activate
# install
pip install -e .
</pre>
                <h4>Command for annotation</h4>
<pre>
export ROBOFLOW_API_KEY= ... 
python -m a2.annotate \
--source_image_directory ... \
--target_annotation_directory ... \
--roboflow_project_id ... \
--roboflow_project_version ...
</pre>
                :warning:API key is a secret key.
                <h4>Annotation Details</h4>
                    <p><b>Annotation type :</b>Bounding Box </p>
                    <p><b>Output File :</b>JSON format</p>
            <h3><li>Creating Training and Testing Dataset</li></h3>
                <h5><b>Train Data</b> : 24,827</h5>
                <h5><b>Test Data</b>  : 15,851</h5>
        </ol>
    <h1><li>TENSORFLOW MODEL CREATION</h1></li>
            <h3><b>Model Used :</b> centernet_resnet50_v2_512x512_coco17_tpu-8</h3>
            <h4><a href="https://github.com/mansiverma19/Indian-Sign-Language-Detection1/blob/main/ISL/indian%20sign%20lang%20model.ipynb"><b>Code File</b></a></h4>
            <ol>
                <li><h4>Download the pre trained model from <a href="http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_resnet50_v2_512x512_coco17">Tensorflow model zoo </a></li>
                <li><h4>Generate the label map for dataset <b>label_map.pbtxt</b></li>
                <li><h4>Generate TF-Record file for Train and Test data</li>
                    <p>Here the file used for generating Tfrecord files are <a href="https://github.com/mansiverma19/Indian-Sign-Language-Detection1/blob/main/ISL/json_generate_tfrecord-1.py">Json generate Tfrecord.py</a> and for converting the labels from json format to csv format <a href="https://github.com/mansiverma19/Indian-Sign-Language-Detection1/blob/main/ISL/json%20to%20csv.py">Json to csv.py</a></p>
                <li><h4>Changing <a href="https://github.com/mansiverma19/Indian-Sign-Language-Detection1/blob/main/ISL%20website/model/pipeline.config">Pipeline.config</a> File for model</h4></li>
                <li><h4>Training the Model </h4></li>
                    <pre>
python ISL\\API\\models\\research\\object_detection\\model_main_tf2.py --model_dir=ISL\\workspace\\models\\CenterNet --   pipeline_config_path=ISL\\workspace\\models\\CenterNet\\pipeline.config --num_train_steps=2000
                    </pre>
                <li><h4>Saving the trained model Checkpoint</h4></li>
                    <pre>
python ISL\API\models\research\object_detection\exporter_main_v2.py  --input_type=image_tensor --pipeline_config_path=ISL\workspace\models\CenterNet\pipeline.config --trained_checkpoint_dir=ISL\workspace\models\CenterNet --output_directory=ISL\workspace\models\CenterNet\output_model5
                    </pre>
            </ol>
    <h1><li>WEB APPLICATION USING FLASK</h1></li>
    <h1><li>Containerization using Docker</li></h1>
            <p>The Web app is converted into a container using the docker images</p>
            <p><a href="https://hub.docker.com/r/mansiverma19/docker-isl">Docker Image of ISL</a></p>
            <pre>
FROM python:3.9

COPY . /app

WORKDIR /app
                
#Installing required packages
RUN pip install opencv-python
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
    adduser appuser video && \
    chown -R appuser /app
USER appuser

EXPOSE 5000

ENV NAME obj_detection

CMD ["python" , "app.py"]
            </pre>
</ol>




