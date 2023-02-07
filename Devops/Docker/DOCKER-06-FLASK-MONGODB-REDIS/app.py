from flask import Flask , render_template,request ,jsonify, Response , redirect ,url_for
import json 
import json2table
from json2html import *
from bson.objectid import ObjectId
import redis
from pymongo import MongoClient 
import os 
import time


app = Flask(__name__)
redisdb=redis.Redis(host='redis-database',port=6379)
mongodb=MongoClient('mongodb-database', 27017)
db=mongodb.flask_db
def mongo_read():
    data=list(db.posts.find())
    for post in data:
        # post["_id"]=str(post["_id"])
        del post["_id"]
    return json.dumps(data)
def mongo_insert(get_post):
    print(get_post,flush=True)
    
    post=json.loads(get_post)
    dbresponse=db.posts.insert_one(post)


    # return Response(
    #     response=json.dumps({"message":"user created"
    #     ,"id":f"{dbresponse.inserted_id}"}),
    #     status=200,
    #     mimetype="application/json"
    # )


def db_init():
    try:
        redisdb.set('foo','bar')
        redisdb.set('mustafa','kurt')
    except:
        print("cant connect")
def db_search(name):
    return redisdb.get(name)

@app.route('/mongoPost',methods=["POST"])
def mongo_page():
    dtestict = request.form
    for key in dtestict:
        mongo_insert(dtestict[key])
        print('form key'+dtestict[key] + '\n', flush=True)
    return jsonify("Post Sended")
        
@app.route('/mongoGet')
def mongo_get():
    return json2html.convert(json=mongo_read())
@app.route('/')
def error():
    return redirect(url_for('main_page'))
@app.route('/login',methods=['GET','POST'])
def main_page():
    if request.method == "POST":
        NAME = request.form['username']
        USER_PASSWORD=request.form['password']
        PASSWORD=db_search(NAME)
        
        if PASSWORD :
                PASSWORD=PASSWORD.decode()
        if str(USER_PASSWORD) == PASSWORD:
            return render_template('secure_page.html',posts=json2html.convert(json=mongo_read()))
        else:
            return render_template('error.html')

    elif request.method =="GET":
        return render_template('index.html')


if __name__=="__main__":
    db_init()
    app.run(host="0.0.0.0",debug=True,port=5000 )
