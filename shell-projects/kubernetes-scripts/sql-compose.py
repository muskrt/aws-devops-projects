#!/bin/python3
import os 
import sys 
import subprocess
import yaml



from pprint import pprint
import base64

def code_base64(data,code_type):
    if code_type == 'encode': 
        data_bytes = data.encode("ascii")
        base64_bytes = base64.b64encode(data_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string
    else:
        base64_bytes = data.encode("ascii")
        data_bytes = base64.b64decode(base64_bytes)
        decodedstring = data_bytes.decode("ascii")
        return decodedstring

def str_presenter(dumper, data):
  if len(data.splitlines()) > 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)
yaml.add_representer(str, str_presenter)
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)

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
def create_secret(vars,name):
    for i in vars:
        vars[i]=code_base64(vars[i],'encode')
    secret=k8_files['secret']
    secret['data']=vars
    secret_name=(name.lower()+'-secret')
    secret['metadata']['name']=secret_name
    f=open(secret_name+'.yaml','w')
    yaml.dump(secret, f, sort_keys=False, default_flow_style=False)
    f.close()
    print('##### secret-created --> ' + f'{secret_name}.yaml')
    return secret_name
    
def create_configmap(volumes,name):
    configmap_names=[]
    for i in volumes:

        for key,value in i.items():
            if (value.__contains__('.sql') and key=='source')  or ( value.__contains__('.cnf') and key=='source'):
                path=value
                filename=path.split('/')[-1]
                check_file = str(subprocess.check_output(f"""
                                if [ -f '{path}' ];
                                then
                                    echo 1
                                else
                                    echo 0
                                fi
                            """, shell=True).decode())
                if int(check_file)==1:
                    configmap=k8_files['configmap']
                    configmap_name=name.lower()+'-'+filename.replace('.','-')+'-configmap'
                    configmap_names.append([configmap_name])
                    
                    
                    # sql_configmap_name=sql_configmap_name.strip('\n')
                    FILE = open(path,'r')
                    file_data=FILE.read()
                    configmap=eval(str(configmap).replace('KEY',filename))
                    configmap=eval(str(configmap).replace('CM',configmap_name))
                    configmap['data'][filename]=file_data
                    f=open(configmap_name+'.yaml','w')
                    yaml.dump(configmap, f, sort_keys=False, default_flow_style=False)
                    f.close()
                    FILE.close()
                    print('##### configmap-created --> ' + f'{configmap_name}.yaml')
                else:
                    print(f'-------------{name}-----------------')
                    print(f'file not found->{value}')
                    print(f'-------------{name}-----------')
        index=0
        for key,value in i.items():
            if (value.__contains__('.sql') and key=='target')  or ( value.__contains__('.cnf') and key=='target'):
                configmap_names[index].append(value)
                index+=1
        del index
    return configmap_names
    
   

def create_deployment(service,name):
    secret_name=''
    configmap_names=[]
    deployment=k8_files['deployment']
    deployment=eval(str(deployment).replace('DEPLOYMENTNAME',name.lower()))

    containers=deployment['spec']['template']['spec']['containers']
    volumes=deployment['spec']['template']['spec']['volumes']

    containers[0]['image']=service['image']
    
    deployment['spec']['template']['spec']['containers'][0]=containers[0]
    deployment['spec']['template']['spec']['volumes'][0]=volumes[0]

    
    if  'volumes' in service:
        configmap_names=create_configmap(service['volumes'],name)
        if configmap_names:
           pass
    if 'environment' in service:
        secret_name=create_secret(service['environment'],name)
        if secret_name:
            print(secret_name)

    # pprint(yaml.dump(deployment))
    # print(compose['services'][i])

     

def main():
    file=open('docker-compose.yml','r')
    test_dict=yaml.load(file, Loader=yaml.FullLoader)
    deployment=k8_files['deployment']
    if '-cs' in sys.argv:
        create_configmap()
    
    SERVICES=test_dict['services']
    for i in SERVICES:
        create_deployment(SERVICES[i],i)
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
