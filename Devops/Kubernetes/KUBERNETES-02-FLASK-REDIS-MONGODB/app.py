from flask import Flask , render_template,request ,jsonify, Response 
import json 
import json2table
from json2html import *
from bson.objectid import ObjectId
import redis
from pymongo import MongoClient 
import os 
import time


app = Flask(__name__)
redisdb=redis.Redis(host='redis',port=6379)
mongodb=MongoClient('mongodb', 27017)
db=mongodb.flask_db
def mongo_read():
    data=list(db.posts.find())
    print(data)
    for post in data:
        # post["_id"]=str(post["_id"])
        del post["_id"]
    return json.dumps(data)
def mongo_insert():
    post={"tag":"mustafa","comment":"kurt"}
    dbresponse=db.posts.insert_one(post)
    post={"tag":"mustafa","comment":"kurt"}
    dbresponse=db.posts.insert_one(post)

    return Response(
        response=json.dumps({"message":"user created"
        ,"id":f"{dbresponse.inserted_id}"}),
        status=200,
        mimetype="application/json"
    )


def db_init():
    try:
        redisdb.set('foo','bar')
        redisdb.set('mustafa','kurt')
    except:
        print("cant connect")
def db_search(name):
    return redisdb.get(name)

@app.route('/mongoPost',methods=["GET","POST"])
def mongo_page():
    if request.method == "POST":
        return mongo_insert()
@app.route('/mongoGet')
def mongo_get():
    return json2html.convert(json=mongo_read())
@app.route('/',methods=['GET','POST'])
def main_page():
    if request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_search(NAME)
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            return render_template('secure_page.html')
        else:
            return render_template('error.html')

    elif request.method =="GET":
        return render_template('index.html')


if __name__=="__main__":
    db_init()
    app.run(host="0.0.0.0",port=5000 )