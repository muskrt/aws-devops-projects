#!/usr/bin/python3
import os 
import sys

def create():
    print('create')
def delete():
    print('delete')

def main():
    os.system('touch ansible.cfg')
    os.system('touch inventory.txt')
   



if __name__=="__main__":
    main()
