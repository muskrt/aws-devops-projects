from flask import Flask , redirect, request, url_for , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html',name='mustafa')

@app.route('/greet', methods=['GET'])
def greet():
    if 'user' in request.args:
        usr= request.args['user']
        return render_template('greet.html',user=usr)
    else:
        return render_template('greet.html',user= 'send your user name'\
        'with "user" param in query ' 
        )

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_name=request.form['username']
        password=request.form['password']
        if password == 'test':
            return render_template('secure.html',user=user_name.title())
        else: 
            return render_template('login.html',user=user_name.title())
    else:
        return render_template('login.html',control=False)

if __name__ == '__main__':
    app.run( host='0.0.0.0',port=80)
