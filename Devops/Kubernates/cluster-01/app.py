from flask import Flask 
import redis 
app=Flask(__name__)
r=redis.Redis(host='localhost',port=6379,db=0)
r.set('foo','bar')
r.get('foo')

@app.route('/')
def main():
    return "welcome"




if __name__=="__main__":
    app.run()