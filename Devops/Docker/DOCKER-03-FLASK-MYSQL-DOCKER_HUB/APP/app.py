from flask import Flask 

app = Flask( __name__)

def db_init():
    app.config['MYSQL_DATABASE_HOST'] = 'database'
    app.config['MYSQL_DATABASE_USER'] = 'mustafa'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'toor1'
    app.config['MYSQL_DATABASE_DB'] = 'bookstore_db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    global mysql 
    mysql = MySQL()
    mysql.init_app(app)
    global connection 
    connection = mysql.connect()
    connection.autocommit(True)
    global cursor 
    cursor = connection.cursor()

def db_get(): pass 
def db_post(): pass 

def login(): pass 
def main_page(): pass 


if __name__=="__main__":
    app.run(debug=True,port=5000)

