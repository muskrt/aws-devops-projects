from flask import Flask , render_template,request,jsonify
import redis
from pymongo import MongoClient 
import os 
import time


app = Flask(__name__)
redisdb=redis.Redis(host='redis',port=6379)
mongodb=MongoClient('mongodb', 27017).flask_db
todos=mongodb.flask_db.todos
mongodb.flask_db.todos.insert_one({'abcd':'abcd'})
def db_init():
    try:
        redisdb.set('foo','bar')
        redisdb.set('mustafa','kurt')
    except:
        print("cant connect")
def db_search(name):
    return redisdb.get(name)
@app.route('/mongo')
def mongo_page():
    return jsonify(todos.find_one('abcd'))
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
