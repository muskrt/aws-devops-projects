#!/bin/bash 
yum update -y 
yum install  subversion -y 
amazon-linux-extras instal docker -y 
systemctl start docker 
systemctl enable docker 
usermod -a -G docker ec2-user 
newgrp docker 
svn export http://github.com/....
sleep 5 
cd dffd 
