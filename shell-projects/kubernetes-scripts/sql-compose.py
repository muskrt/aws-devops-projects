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
    k8_file_names=['deployment','service','secret','configmap','hpa']
    k8_files={'deployment':{},'service':{},'secret':{},'configmap':{},'hpa':{}}
    for i in k8_file_names:
        print(k8_files[i])
    src_paths=['k8-config-files/deployment.yaml','k8-config-files/service.yaml','k8-config-files/secret.yaml','k8-config-files/configmap.yaml','k8-config-files/hpa.yaml']
    exit()





if __name__=="__main__":
    main()
