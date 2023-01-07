from flask import Flask 
import redis 
app=Flask(__name__)
r=redis.Redis(host='database',port=6379,db=0)
def init_db():

    r.set('foo','bar')
    return r.get('foo')

@app.route('/')
def root():
    return init_db()



if __name__=="__main__":
    init_db()
    app.run(host='0.0.0.0',port=5000)