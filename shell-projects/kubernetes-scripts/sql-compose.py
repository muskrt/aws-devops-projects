#!/bin/python3
import os 
import sys 
import yaml
from pprint import pprint

def main():
    file=open('docker-compose.yml','r')
    test_dict=yaml.load(file, Loader=yaml.FullLoader)
    # pprint(test_dict['services'])
    for i in test_dict['services']:
        print(i)
    


if __name__=="__main__":
    main()
