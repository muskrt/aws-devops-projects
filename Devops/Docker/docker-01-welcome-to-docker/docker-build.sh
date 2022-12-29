#!/bin/bash
amazon-linux-extras install docker -y
systemctl docker start 
systemctl enable docker  
usermod -a -G docker ec2-user 
newgrp docker 
cd App
docker image build -t muskrt/welcomeapp:1.0 .
docker container run --rm -dit --network host --name myapp muskrt/welcomeapp:1.0
