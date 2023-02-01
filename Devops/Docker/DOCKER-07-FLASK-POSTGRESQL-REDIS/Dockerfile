# Name=muskrt/kubernetes-03-app 
FROM python:alpine
RUN apk update 
WORKDIR /APP 
COPY requirements.txt requirements.txt 
RUN  pip install requirements.txt 
COPY . . 
CMD python app.py 
