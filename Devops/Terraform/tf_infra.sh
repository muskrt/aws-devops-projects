#!/bin/bash 
file_to_create_workspace=''
files_to_create=(main.tf providers.tf outputs.tf mustafa.auto.tfvars variable.tf)
# for file in ${files_to_create[@]};
# do 
# echo $file 
# done 
# exit 1

for var in "$@";
do  

if [[ ${#var} -gt 2 ]]
    then 
        echo TEST 
    else 
        echo $var 
    fi 


done


name=$1
IFS="="
read -ra ADDR<<<"$name" 
for i in "${ADDR[1]}";
do
echo "$i"
done


