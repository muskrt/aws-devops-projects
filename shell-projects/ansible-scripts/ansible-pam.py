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
    file=open('inventory.txt','r')
    group=''
    for line in file.readline():
        print(line)
    file.close()

   



if __name__=="__main__":
    main()
