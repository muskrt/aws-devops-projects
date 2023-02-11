#!/bin/bash
yum update -y
amazon-linux-extras install docker -y
systemctl start docker
systemctl enable docker
usermod -a -G docker ec2-user
newgrp docker
curl -L "https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
cd /home/ec2-user/
until ls App
do 
    echo "waiting for files..."
done 

# while [  true ]; do  docker-compose up 2>/dev/null && break || continue;  done
until docker-compose up 2>/dev/null
    do 
        echo "waiting for docker-compose..."
        sleep 1 
    done 

