
from flask import Flask ,render_template, redirect, url_for 

app = Flask(__name__)

@app.route('/about')
def about():
    return '<h1>This is my about page</h1>'

@app.route('/')
def home():
    return "This is home page for no path , <h1> Welcome home</h1>"

@app.route('/error')
def error():
    return "<h1>Either you encountered a problem or you are not authorized. </h1>"


@app.route('/admin')
def admin():
    return redirect(url_for('error'))

@app.route('/<name>')
def greet(name):
    authorizied_personel=['mustafa','jonathon','Tpol','Trip']
    return render_template('greet.html', name=name, personel=authorizied_personel)

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet' ,name="mustafa"))

@app.route('/list10')
def list10():
    return render_template('list10.html')

@app.route('/evens')
def evens():
    return render_template('evens.html')
if __name__=="__main__":
    app.run(debug=True,port=5000)