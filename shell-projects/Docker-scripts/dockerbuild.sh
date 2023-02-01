#!/bin/bash 
CWD=`pwd`
echo $CWD
tag=`cat Dockerfile | grep Name | cut -d'=' -f2`
echo $tag