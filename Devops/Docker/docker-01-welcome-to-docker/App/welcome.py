from flask import Flask

app=Flask(__name__)


@app.route('/')
def main():
    return "welcome to the test application of docker.<h3>Created By Mustafa kurt.</h3>"
@app.route('/about'):
def about_page():
    return "this is the about page of sample application.<h3>Created By Mustafa Kurt.</h3>"
if __name__=="__main__":
    app.run(debug=True,port=80)



