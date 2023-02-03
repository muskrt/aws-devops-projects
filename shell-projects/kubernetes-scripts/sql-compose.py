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
    secret['metadata']['name']=(name.lower()+'-secret')
    print(secret)

    
def create_configmap():
    SQL_FILE = str(subprocess.check_output("ls *.sql", shell=True).decode())
    configmap=k8_files['configmap']
    global sql_configmap_name
    sql_configmap_name=SQL_FILE.replace('.','-')
    sql_configmap_name=sql_configmap_name.strip('\n')
    FILE = open(SQL_FILE.strip('\n'),'r')
    sqldata=FILE.read()
    configmap=eval(str(configmap).replace('KEY',SQL_FILE.strip('\n')))
    configmap=eval(str(configmap).replace('CM',sql_configmap_name))
    configmap['data'][SQL_FILE.strip('\n')]=sqldata
    f=open(sql_configmap_name+'-configmap.yaml','w')
    yaml.dump(configmap, f, sort_keys=False, default_flow_style=False)
    f.close()
    FILE.close()
    
    CNF_FILE = str(subprocess.check_output("ls *.cnf", shell=True).decode())
    configmap=k8_files['configmap']
    global cnf_configmap_name
    cnf_configmap_name=CNF_FILE.replace('.','-')
    cnf_configmap_name=cnf_configmap_name.strip('\n')
    FILE = open(CNF_FILE.strip('\n'),'r')
    cnfdata=FILE.read()
    configmap=eval(str(configmap).replace('KEY',CNF_FILE.strip('\n')))
    configmap=eval(str(configmap).replace('CM',cnf_configmap_name))
    configmap['data'][CNF_FILE.strip('\n')]=cnfdata
    f=open(cnf_configmap_name+'-configmap.yaml','w')
    yaml.dump(configmap, f, sort_keys=False, default_flow_style=False)
    f.close()
    FILE.close()



    # CNF_FILE = str(subprocess.check_output("ls *.cnf", shell=True).decode())


    # sqldata = sqldata.encode('unicode_escape').decode()


    # print(sqldata)
    

def create_deployment(compose,i):
    deployment=k8_files['deployment']
    deployment['spec']['template']['spec']['containers'][0]['image']=compose['services'][i]['image']
    deployment=eval(str(deployment).replace('DEPLOYMENTNAME',i.lower()))
    
    if 'environment' in compose['services'][i]:
        create_secret(compose['services'][i]['environment'],i)

    # pprint(yaml.dump(deployment))
    # print(compose['services'][i])

     

def main():
    file=open('docker-compose.yml','r')
    test_dict=yaml.load(file, Loader=yaml.FullLoader)
    deployment=k8_files['deployment']
    if '-cs' in sys.argv:
        create_configmap()
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
