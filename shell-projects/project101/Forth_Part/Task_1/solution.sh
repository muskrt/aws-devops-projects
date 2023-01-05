#!/bin/bash
##solution1
str=$(cat info.json | grep PrivateIpAddress | head -1 | grep -Eo "[0-9]+.[0-9]+.[0-9]+.[0-9]+")
sed "s/ec2-private_ip/$str/g" terraform.tf 
##solution2
sed -i "s/ec2-private_ip/$(grep PrivateIpAddress info.json | head -n1 | cut -d'"' -f4)/g" terraform.tf
