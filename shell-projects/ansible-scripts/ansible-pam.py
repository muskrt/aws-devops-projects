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
    
    os.system('touch inventory.txt')
   



if __name__=="__main__":
    create()
