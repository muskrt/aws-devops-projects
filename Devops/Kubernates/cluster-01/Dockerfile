FROM python:alpine 
RUN apk update 
WORKDIR /App/ 
COPY ./requirements.txt /App/
RUN pip install -r requirements.txt 
COPY . /App/
CMD python welcome.py