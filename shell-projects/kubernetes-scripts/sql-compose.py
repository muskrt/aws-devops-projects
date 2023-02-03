#!/bin/python3
import os 
import sys 
import yaml
from pprint import pprint

def prepare_templates():
    k8_file_names=['deployment','service','secret','configmap','hpa']
    global k8_files
    k8_files={'deployment':{},'service':{},'secret':{},'configmap':{},'hpa':{}}

    src_paths=['k8-config-files/deployment.yaml','k8-config-files/service.yaml','k8-config-files/secret.yaml','k8-config-files/configmap.yaml','k8-config-files/hpa.yaml']
    for name in k8_file_names:
        file=open(src_paths[ k8_file_names.index(name)])
        k8_files[name]=file.read()
        file.close()

def main():
    file=open('docker-compose.yml','r')
    test_dict=yaml.load(file, Loader=yaml.FullLoader)
    # pprint(test_dict['services'])


    





if __name__=="__main__":
    main()
