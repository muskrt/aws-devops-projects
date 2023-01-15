from flask import Flask 

app = Flask(__name__)

def init_db(): pass 
def db_get(sourcedb=''): pass 
def db_insert(sourcedb=''): pass 
def db_delete(sourcedb=''): pass 
def db_update(sourcedb=''): pass 

def update(): pass 
def delete(): pass 
def post(): pass 
def get(): pass 


if __name__=="__main__":
    app.run()