from flask import Flask, render_template
from flask import url_for
from flask import request
from config import host, user, password, db_name
import psycopg2


app = Flask(__name__)
def get_db_connection(): 
    conn = psycopg2.connect(
        host=host,
        dbname=db_name,
        user=user,
        password=password)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/submit', methods=("GET","POST"))
def submit():
    try:
        if request.method=="POST":
            name= request.form['Name']
            position= request.form['Position']
            salary= int(request.form['Salary'])
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('insert into employees (name, position, salary)' 
                'values(%s, %s, %s)',
                (name, position, salary))
            conn.commit()
            cur.close()
            conn.close()
        return(index())
    except:
        return index()


@app.route('/delete', methods=("GET","POST"))
def delete():
    sql="DELETE from employees WHERE id= %s"
    try:
        if request.method=="POST":
            id= request.form['ID']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(sql, (id,))
            conn.commit()
            cur.close()
            conn.close() 
        return(index())
    except:
        return index()
