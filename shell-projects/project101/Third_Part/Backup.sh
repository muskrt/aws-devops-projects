#!/bin/bash


if  [  $UID -ne  0  ]
then 
echo "run as root"
fi

src=" /home/nate/Desktop/aws-devops-projects/shell-scripts/project101/Third_Part/data /home/nate/Desktop/aws-devops-projects/shell-scripts/project101/Third_Part/data1"
dst="/home/nate/Desktop/aws-devops-projects/shell-scripts/project101/Third_Part/"
time=$(date +'%Y_%m_%d_%H_%M')
hostname=$(hostname -s)
archive_file="$hostname-$time.tgz"
echo "archive process is started"

tar -czf $dst/$archive_file $src 


