from flask import Flask , render_template, request, url_for
import redis 
import psycopg2


app = Flask(__name__)

def init_db():
    global REDISDB 
    REDISDB=redis.Redis(host='redis-db',port=6379)
    global POSTGREDB
    conn = psycopg2.connect(
            host="postgre-db",
            database="flask_db",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
    conn.set_session(autocommit=True)
    POSTGREDB= conn.cursor(withhold=True)
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

def db_get(sourcedb=''): pass 
def db_insert(sourcedb=''): pass 
def db_delete(sourcedb=''): pass 
def db_update(sourcedb=''): pass 

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')  
    elif request.method == "POST":
        return render_template('secure_page.html')
    
    
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
    app.run(host="0.0.0.0")