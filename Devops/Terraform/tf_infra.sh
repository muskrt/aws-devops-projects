#!/bin/bash 
file_to_create_workspace=''
files_to_create=[main.tf,providers.tf,outputs.tf,mustafa.auto.tfvars,variable.tf]

IFS="="
read -ra ADDR<<<"$name" 
for i in "${ADDR[@]}";
do
echo "$i"
done


