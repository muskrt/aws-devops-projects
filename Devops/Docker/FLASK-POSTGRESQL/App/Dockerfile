FROM python:alpine 
WORKDIR /app
ENV DB_USERNAME=nate DB_PASSWORD=postgretoor

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 
COPY . . 
CMD python app.py 