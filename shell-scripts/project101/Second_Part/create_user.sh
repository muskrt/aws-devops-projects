#!/bin/bash


if [ $UID -ne 0 ]
then
echo -e "Run as root."
exit 1
else
echo -e "YOU are running this script as root.\n\n"
fi


read -p "Enter username: " username
read -p "Enter Comment: " comment
echo $username 
password=$(echo $RANDOM | md5sum | head -c 20)

useradd -c $comment -m $username 

if [ $? -eq 0 ]
then 
echo "user created"
echo -e "\nUsername: $username\nPassword: $password\n"
else 
echo "can't create user"
fi
echo -e "$password\n$password" | passwd  $username
passwd -e $username


