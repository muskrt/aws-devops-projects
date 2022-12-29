#!/bin/python3
from flask import Flask , render_template ,url_for, redirect


app = Flask(__name__)



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login')
def redirect_for_login():
    return redirect(url_for('login'))

@app.route('/mainpage.html')
def main_page():
    return render_template("mainpage.html")


if __name__ =="__main__":
    app.run(debug=True,port=5000)
