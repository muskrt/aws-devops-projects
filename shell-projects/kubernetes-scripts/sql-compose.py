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
        k8_files[name]=yaml.load(file, Loader=yaml.FullLoader)
        file.close()
def main():
    file=open('docker-compose.yml','r')
    test_dict=yaml.load(file, Loader=yaml.FullLoader)
    for i in test_dict['services']:
        pprint(test_dict['services'][i])
        
    deployment=k8_files['deployment']
    pprint(deployment['spec']['template']['spec']['containers'][0]['env'])
    exit()
    file=open('testdeployment.yaml','w')
    file.write(deployment)
    file.close()


    





if __name__=="__main__":
    prepare_templates()
    main()
