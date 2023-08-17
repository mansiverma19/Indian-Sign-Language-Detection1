FROM python:3.9

#copy the content of current directory to /app
COPY . /app

#use working directory /app
WORKDIR /app

#Installing required packages
RUN pip install opencv-python
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --trusted-host pypi.python.org -r requirements.txt


RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
    adduser appuser video && \
    chown -R appuser /app
USER appuser

#Open port 5000
EXPOSE 5000

#Set env variable
ENV NAME obj_detection

#Run python app 
CMD ["python" , "app.py"]