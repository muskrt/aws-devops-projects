#!/bin/python3
import os 
import sys 
import subprocess
import yaml
from pprint import pprint
import base64

def prepare_templates():
    k8_file_names=['deployment','service','secret','configmap','hpa']
    global k8_files
    k8_files={'deployment':{},'service':{},'secret':{},'configmap':{},'hpa':{}}

    src_paths=['k8-config-files/deployment.yaml','k8-config-files/service.yaml','k8-config-files/secret.yaml','k8-config-files/configmap.yaml','k8-config-files/hpa.yaml']
    for name in k8_file_names:
        file=open(src_paths[ k8_file_names.index(name)])
        k8_files[name]=yaml.load(file, Loader=yaml.FullLoader)
        file.close()
def create_service():
    pass 
def create_secret(vars):
    print(vars)
    
def create_configmap():
    files = str(subprocess.check_output("ls *.sql", shell=True).decode())
    print('------',files)
def create_deployment(compose,i):
    deployment=k8_files['deployment']
    deployment['spec']['template']['spec']['containers'][0]['image']=compose['services'][i]['image']
    deployment=eval(str(deployment).replace('DEPLOYMENTNAME',i.lower()))
    
    if 'environment' in compose['services'][i]:
        create_secret(compose['services'][i]['environment'])
    if '-cs' in sys.argv:
        create_configmap()
    # pprint(yaml.dump(deployment))
    # print(compose['services'][i])

     

def main():
    file=open('docker-compose.yml','r')
    test_dict=yaml.load(file, Loader=yaml.FullLoader)
    deployment=k8_files['deployment']
    for i in test_dict['services']:
        create_deployment(test_dict,i)
        # deployment['spec']['template']['spec']['containers'][0]['image']=test_dict['services'][i]['image']
        # deployment=eval(str(deployment).replace('DEPLOYMENTNAME',i.lower()))
        # pprint(yaml.dump(deployment))
        # print(test_dict['services'][i])


        
        # f=open('testDeployment.yaml','w')
        # yaml.dump(deployment, f, sort_keys=False, default_flow_style=False)
        # break
        # pprint(test_dict['services'][i])
        
    
    
    exit()
    file=open('testdeployment.yaml','w')
    file.write(deployment)
    file.close()


    





if __name__=="__main__":
    prepare_templates()
    main()
