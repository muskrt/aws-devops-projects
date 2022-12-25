#!/bin/bash 
yum update -y 
yum install python3 -y 
yum install subversion -y 
svn export https://github.com/muskrt/aws-devops-projects.git/trunk/python-projects/flask-05-handling-sql-with-web-application
cd flask-05-handling-sql-with-web-application
pip3 install -r requirements.txt
python3 app-with-mysql.py