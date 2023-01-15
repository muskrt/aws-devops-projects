from flask import Flask , render_template, url_for, request

app = Flask(__name__)

def db_init():pass 
def db_delete(sourcedb=''): pass 
def db_update(sourcedb=''): pass 
def db_get(sourcedb=''): pass 
def db_insert(sourcedb=''): pass 

@app.route('/update')
def update(): 
    pass 
@app.route('/delete')
def delete():
     pass 

@app.route('/', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    elif request.method == "POST"
        USERNAME=request.params['username']
        PASSWORD=request.params['password']
        if USERNAME == '' and PASSWORD == '':
            return render_template('secure_page.html')
        else:
            return render_template('error.html')




if __name__=="__main__":
    app.run()