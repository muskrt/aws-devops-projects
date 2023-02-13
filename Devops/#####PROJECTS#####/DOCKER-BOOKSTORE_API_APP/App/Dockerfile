FROM python:alpine
RUN apk update && apk add bash
SHELL ["/bin/bash","-c"]
WORKDIR /APP 
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 
COPY . . 
CMD python bookstore-api.py 
