#!/usr/bin/python
from flask import Flask , render_template, url_for, request
import redis 
import mariadb 
from json2html import *
app = Flask(__name__)
def db_init():
    # mariadb
    config = {
    'host': 'mariadb',
    'port': 3306,
    'user': 'mustafa',
    'password': 'toor1',
    'database': 'abc_company'
    }
    global MARIADB 
    MARIADBCON =mariadb.connect(**config)
    MARIADBCON.autocommit = True
    MARIADB=MARIADBCON.cursor()
    
    # redis 
    global REDISDB 
    REDISDB=redis.Redis(host='redisdb',port=6379)
    REDISDB.set('mustafa','kurt')

def db_get(sourcedb,query_string): 
    if sourcedb =="REDISDB":
        return REDISDB.get(query_string[0])
    elif  sourcedb =="MARIADB":
        MARIADB.execute(query_string)
        data=[]
        for i in MARIADB:
            print("--------db server data------",i)
            data.append(i)
        return data

def db_delete(sourcedb,query_string): 
    if sourcedb =="REDISDB":
        REDISDB.delete(query_string[0],query_string[1])
    elif sourcedb=="MARIADB":
        MARIADB.execute()

def db_update(sourcedb,query_string): 
    if sourcedb =="REDISDB":
        REDISDB.set(query_string[0],query_string[1])
    elif sourcedb=="MARIADB":
        MARIADB.execute()

def db_insert(sourcedb,query_string): 
    if sourcedb =="REDISDB":
        REDISDB.set(query_string[0],query_string[1])
    elif sourcedb=="MARIADB":
        MARIADB.execute()

@app.route('/add_admin', methods=['GET','POST'])
def add_admin():
    if request.method =='GET':
        return render_template('add_admin.html')
    elif request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_get("REDISDB",NAME)
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            return render_template('secure_page.html')
        else:
            return render_template('error.html')

@app.route('/delete_admin', methods=['GET','POST'])
def delete_admin():
    if request.method =='GET':
        return render_template('delete_admin.html')
    elif request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_get("REDISDB",NAME)
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            return render_template('secure_page.html')
        else:
            return render_template('error.html')

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method =='GET':
        return render_template('add.html')
    elif request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_get("REDISDB",NAME)
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            return render_template('secure_page.html')
        else:
            return render_template('error.html')

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method =='GET':
        return render_template('update.html')
    elif request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_get("REDISDB",NAME)
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            return render_template('secure_page.html')
        else:
            return render_template('error.html')

@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method =='GET':
        return render_template('delete.html')
    elif request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_get("REDISDB",NAME)
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            return render_template('secure_page.html')
        else:
            return render_template('error.html')

@app.route('/', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    elif request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_get("REDISDB",[NAME,'test'])
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            db_data_offices=db_get("MARIADB","SELECT * FROM  offices;")
            db_data_employees=db_get("MARIADB","SELECT * FROM  employees;")
            return render_template('secure_page.html',offices=db_data_offices,employees=db_data_employees)
            
        else:
            return render_template('error.html')
            


if __name__=="__main__":
    db_init()
    app.run(host="0.0.0.0")