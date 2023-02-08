#!/bin/bash
yum update -y 
yum install python3 -y 
pip3 install flask 
pip3 install flask_mysql 
cd /home/ec2-user
yum install subversion -y
svn export https://github.com/muskrt/aws-devops-projects.git/trunk/Devops/PROJECTS/TERRAFORM-PHONEBOOK_APP-AWS_DEPLOYMENT/APP
cd APP
python3 phonebook-app.py 
