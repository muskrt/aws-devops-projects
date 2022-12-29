#!/bin/bash
amazon-linux-extras install docker -y
systemctl start docker  
systemctl enable docker  
usermod -a -G docker ec2-user 
newgrp docker 
docker image build -t muskrt/welcomeapp:1.0 -f /home/ec2-user/docker-01-welcome-to-docker/App/
docker container run --rm -dit --network host --name myapp muskrt/welcomeapp:1.0
