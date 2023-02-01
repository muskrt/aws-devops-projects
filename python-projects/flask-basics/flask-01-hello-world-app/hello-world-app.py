from flask import Flask

app=Flask(__name__)


@app.route('/')
def main():
    return "welcome to Flask"

@app.route('/second')
def second():
    return "You are in the sub-page of root named second."

@app.route('/third/subthird')
def sub_third():
    return "You are in sub-page of third named subthird." 

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'

if __name__=="__main__":
    app.run(debug=True,port=5000)



