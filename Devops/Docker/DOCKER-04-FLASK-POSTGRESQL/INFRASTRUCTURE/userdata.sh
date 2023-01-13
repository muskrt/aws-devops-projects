#!/bin/bash
yum update -y 
yum install subversion -y 
yum install amazon-linux-extras docker 
usermod -a -G docker $USER 
newgrp docker 
svn export ... 
cd .../.... 
docker build -t myImage . 
docker container run -dit -p 80:5000 --network host --name myApp myImage 
