# Name=muskrt/kubernetes-04-bookworm_api 
FROM python:alpine
RUN apk update && apk add bash
# ENTRYPOINT /bin/bash
SHELL ["/bin/bash", "-c"]
WORKDIR /APP 
COPY requirements.txt requirements.txt 
RUN  pip install -r  requirements.txt 
COPY . . 
CMD python app.py 
