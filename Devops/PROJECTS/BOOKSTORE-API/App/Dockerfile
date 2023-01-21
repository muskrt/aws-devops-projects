FROM python:alpine
COPY requirements.txt /APP/requirements.txt 
WORKDIR /APP 
RUN pip install -r requirements.txt 
COPY . . 
CMD python bookstore-api.py 
