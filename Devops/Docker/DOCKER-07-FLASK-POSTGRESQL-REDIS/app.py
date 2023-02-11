from flask import Flask , render_template, request, url_for
import redis 
import psycopg2
import os 
import sys


app = Flask(__name__)

def init_db():
    global REDISDB 
    REDISDB=redis.Redis(host='redis-db',port=6379)
    global POSTGREDB
    conn = psycopg2.connect(
            host="postgre-db",
            database="bookworm_api_db",
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'])
    conn.set_session(autocommit=True) 
    POSTGREDB= conn.cursor()
    POSTGREDB.execute('DROP TABLE IF EXISTS books;')
    POSTGREDB.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                    'title varchar (150) NOT NULL,'
                                    'author varchar (50) NOT NULL,'
                                    'pages_num integer NOT NULL,'
                                    'review text,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                    )

    POSTGREDB.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('A Tale of Two Cities',
                'Charles Dickens',
                489,
                'A great classic!')
                )
    POSTGREDB.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Anna Karenina',
                'Leo Tolstoy',
                864,
                'Another great classic!')
                )
def db_get(sourcedb,query_string):
    if sourcedb =="REDISDB":
        return REDISDB.get(query_string[0])
    elif  sourcedb =="POSTGREDB":
        POSTGREDB.execute(query_string)
        data=[]
        for i in POSTGREDB:
            data.append(i)
        return data
def db_insert(sourcedb,query_string):
    if sourcedb =="REDISDB":
        return REDISDB.set(query_string[0],query_string[1])
    elif  sourcedb =="POSTGREDB":
        POSTGREDB.execute(query_string)
        # data=[]
        # for i in POSTGREDB:
        #     print("--------db server data------",i)
        #     data.append(i)
        # return data 
def db_delete(sourcedb=''): pass 
def db_update(sourcedb=''): pass 

@app.route('/add',methods=['GET','POST'])
def add_to_unread():
    pass 

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')  
    elif request.method == "POST":
        if 'addtest' in  request.form.to_dict().keys():
            print(request.form['addtest'],flush=True)
        data=db_get('POSTGREDB','select * from books;')
        return render_template('secure_page.html',data = data)
    
    
@app.route('/update')
def update(): 
    pass
@app.route('/delete') 
def delete(): 
    pass 
@app.route('/add')
def add():
    pass 
    


if __name__=="__main__":
    init_db()
    app.run(host="0.0.0.0",debug=True)