from flask import Flask , render_template,request
import redis 
app=Flask(__name__)
r=redis.Redis(host='database',port=6379,db=0)
r.set('foo','bar')
r.set('mustafa','kurt')
def db_search(name='foo'):
    return r.get(name)

@app.route('/',methods=['GET','POST'])
def main_page():
    if request.method == "POST":
        NAME = str(request.form.get("username"))
        PASSWORD=str(request.form.get("password"))
        if db_search(NAME) == PASSWORD:
            return "success"
        else:
            return "failed"
    elif request.method =="GET":
        return render_template('index.html')



if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)