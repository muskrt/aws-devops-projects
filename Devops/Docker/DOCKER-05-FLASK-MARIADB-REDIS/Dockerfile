FROM python:alpine
RUN apk update 
RUN apk add libc-dev 
RUN apk add python3-dev
RUN apk add gcc 
# Name=muskrt/kubernetes-01-app
RUN apk add mariadb-connector-c mariadb-connector-c-dev
RUN apk add  mariadb-client
WORKDIR /APP
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY . . 
CMD python app.py
