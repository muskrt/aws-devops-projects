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
    k8_files = {
    'deployment':
    {'apiVersion': 'apps/v1', 'kind': 'Deployment', 
    'metadata': {'name': 'DEPLOYMENTNAME', 'labels': {'name': 'DEPLOYMENTNAME'}}, 
    'spec': {
    'selector':{
    'matchLabels':{
    'name': 'DEPLOYMENTNAME'}},'replicas': 2, 
    'strategy': {'rollingUpdate': {'maxSurge': 1, 'maxUnavailable': 1}, 'type': 'RollingUpdate'}, 
    'template': {'metadata': {'labels': {'name': 'DEPLOYMENTNAME'}}, 
    'spec': {
    'containers': [{
    'image': 'IMAGENAME','imagePullPolicy': 'Always', 'name': 'DEPLOYMENTNAME', 
    'livenessProbe':{'httpGet':{'path': '/health','port': 5000},'initialDelaySeconds': 20,'periodSeconds': 5},
    'resources': {'limits': {'cpu': '200m', 'memory': '250Mi'}}, 
    'env': [{'name': 'MARIADB_PASSWORD', 'valueFrom': {'secretKeyRef': {'name': 'user-password', 'key': 'db-password'}}}],
    'ports': [{'containerPort': 5000}], 
    'volumeMounts': [{'name': 'config', 'mountPath': 'DESTINATION','subPath':'filename'}]}],
    'restartPolicy': 'Always',
    'volumes': [{
    'name': 'SQL-CONFIG', 'configMap': {
    'name': 'CONFIGMAPNAME','items':[{'key':'cmkey','path':'filename'}]}
    }]}}}},
    'service':
    {'kind': 'Service', 'apiVersion': 'v1',
    'metadata': {'name': 'Service Name','labels':{'name': 'Deploymentname'}}, 
    'spec': {
    'selector': {'app': 'Selector Label'}, 
    'type': 'NodePort', 'ports': [{
    'name': 'name-of-the-port', 'port': 80, 'targetPort': 8080}]}},
    'secret':
    {'apiVersion': 'v1', 'kind': 'Secret',
    'metadata': {'name': 'secretName'},
    'data': {'secretKey': 'BASE64_ENCODED_VALUE'}, \
    'type': 'Opaque'},
    'configmap':
    {'kind': 'ConfigMap', 'apiVersion': 'v1', 
    'metadata': {'name': 'CM', 'namespace': 'default'}, 
    'data': {'KEY': 'SQLDATA\n'}},
    'hpa':
    {'apiVersion': 'autoscaling/v2', 'kind': 'HorizontalPodAutoscaler', 
    'metadata': {'name': 'myapp'}, 
    'spec': {'scaleTargetRef': {'apiVersion': 'apps/v1', 'kind': 'Deployment', 'name': 'myapp'}, 'minReplicas': 1,
    'maxReplicas': 3, 'metrics': [{
    'type': 'Resource', 
    'resource': {
    'name': 'cpu', 'target': {'type': 'Utilization', 'averageUtilization': 50}}}]}}
    }

    # src_paths=['k8-config-files/deployment.yaml','k8-config-files/service.yaml','k8-config-files/secret.yaml','k8-config-files/configmap.yaml','k8-config-files/hpa.yaml']
    # for name in k8_file_names:
    #     file=open(src_paths[ k8_file_names.index(name)])
    #     k8_files[name]=yaml.load(file, Loader=yaml.FullLoader)
    #     file.close()
def create_service(service,name):
    k8_service=k8_files['service']

    k8_service_name=(name.lower()+'-service')
    k8_service['metadata']['name']=name.lower()
    k8_service['metadata']['labels']['name']=name.lower()

    k8_service['spec']['selector']={'name':f'{name.lower()}'}
    k8_service['spec']['ports'][0]['name']=service['ports'][0].split(':')[1]
    k8_service['spec']['ports'][0]['port']=int(service['ports'][0].split(':')[0])
    k8_service['spec']['ports'][0]['targetPort']=int(service['ports'][0].split(':')[1])
    f=open(k8_service_name+'.yaml','w')
    yaml.dump(k8_service, f, sort_keys=False, default_flow_style=False)
    f.close()
    print('##### service-created --> ' + f'{k8_service_name}.yaml') 
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
    return secret_name,vars
    
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
    for i in volumes:
        for key,value in i.items():
            
            if (value.__contains__('.sql') and key=='target'):
                configmap_names[index].append(value)
                index+=1
            elif ( value.__contains__('.cnf') and key=='target'):
                configmap_names[index].append(value)
                index+=1
    del index
    return configmap_names
    
   

def create_deployment(service,name):
    secret_name=''
    configmap_names=[]
    deployment=k8_files['deployment'].copy()
     
    deployment=eval(str(deployment).replace('DEPLOYMENTNAME',name.lower()))

    containers=deployment['spec']['template']['spec']['containers']
    volumes=deployment['spec']['template']['spec']['volumes']
    volume_mounts=deployment['spec']['template']['spec']['containers'][0]['volumeMounts']
    if name.__contains__('db'):
        del deployment['spec']['template']['spec']['containers'][0]['livenessProbe'] 
    else:
        pass  
    
    env=deployment['spec']['template']['spec']['containers'][0]['env']
    deployment['spec']['template']['spec']['containers'][0]['ports'][0]['containerPort']=int(service['ports'][0].split(':')[1])


    containers[0]['image']=service['image']
    

    
    if  'volumes' in service:
        configmap_names=create_configmap(service['volumes'],name)
        volume_mounts_from_cm=[]
        volume_from_cm=[]
        
        if configmap_names:
            for i in configmap_names:
                volume_name=str(i[0]).split('-')[2]
                volume_mount={'name': f'{volume_name}', 'mountPath': f'{i[1]}','subPath':f'{(i[1]).split("/")[-1]}'}
                volume={'name': f'{volume_name}', 'configMap': {'name':  f'{i[0]}','items':[{'key':f'{(i[1]).split("/")[-1]}','path':f'{(i[1]).split("/")[-1]}'}]}}
                volume_mounts_from_cm.append(volume_mount)
                volume_from_cm.append(volume)
            volume_mounts=volume_mounts_from_cm
            volumes=volume_from_cm
            deployment['spec']['template']['spec']['volumes']=volumes
            deployment['spec']['template']['spec']['containers'][0]['volumeMounts']=volume_mounts
        else:
            del deployment['spec']['template']['spec']['volumes']
            del deployment['spec']['template']['spec']['containers'][0]['volumeMounts'] 
    else:
        del deployment['spec']['template']['spec']['volumes']
        del deployment['spec']['template']['spec']['containers'][0]['volumeMounts'] 
    if 'environment' in service:
        secret_name,env_vars=create_secret(service['environment'],name)
        if secret_name:
            env_from_sk=[]
            for key,value in env_vars.items():
                env={'name': f'{key}', 'valueFrom': {'secretKeyRef': {'name': f'{secret_name}', 'key': f'{key}'}}}
                env_from_sk.append(env)
            env=env_from_sk
            deployment['spec']['template']['spec']['containers'][0]['env']=env
    else :
        del deployment['spec']['template']['spec']['containers'][0]['env']
    deployment['spec']['template']['spec']['containers'][0]=containers[0]
    


    f=open(name.lower()+'-deployment.yaml','w')
    yaml.dump(deployment, f, sort_keys=False, default_flow_style=False)
    f.close()
    print('##### Deployment-created --> ' + f'{name.lower()}-deployment.yaml')

     

def main():
    file=open('docker-compose.yml','r')
    test_dict=yaml.load(file, Loader=yaml.FullLoader)
    deployment=k8_files['deployment']
    SERVICES=test_dict['services']
    for i in SERVICES:
        create_service(SERVICES[i],i)
        create_deployment(SERVICES[i],i)
  

if __name__=="__main__":
    prepare_templates()
    main()
