from flask import Flask 

app = Flask( __name__)

def db_init(): pass 
def db_get(): pass 
def db_post(): pass 

def login(): pass 
def 

@app.route('/')
def main_page():
    return "test"




if __name__=="__main__":
    app.run(debug=True,port=5000)

