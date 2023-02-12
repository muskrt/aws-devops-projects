#!/usr/bin/python3
import os 
import sys

def create():
    file=open('ansible.cfg','w')
    file.write("test")
    file.close()
    print('success')
def delete():
    print('delete')

def main():
    file=open('temporary.txt','r')
    content=file.read()
    group_names=set()
    groups={}

    for i in content.split('\n'):
        if len(i.split('-')[0])>1:
            group_names.add(i.split('-')[0])

    for i in group_names:
        groups[i]=[]

    for i in content.split('\n'):
        group_name=i.split('-')[0]
        if len(group_name)>1:
            if group_name in group_names:
                # groups[group_name].append(i)
                i=i.split(' ')
                i=(i[0]+" ansible_host="+i[1]+" ansible_user=ec2-user")
                groups[group_name].append(i)
    exit()
    with open('inventory.txt','a') as file:
        for key in groups:
            file.write('['+key+']\n')
            for value in groups[key]:
                file.write(value+'\n')
        file.close()
    file.close()

   



if __name__=="__main__":
    main()
