# Name=muskrt/kubernetes-02-app
FROM python:3.7-alpine 
WORKDIR /code 
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt  
EXPOSE 5000
COPY . .

CMD python app.py
