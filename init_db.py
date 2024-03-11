import os
import psycopg2
from config import host, user, password, db_name

conn = psycopg2.connect(
        host=host,
        dbname=db_name,
        user=user,
        password=password)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS employees;')
cur.execute('CREATE TABLE employees (id serial PRIMARY KEY,'
                    'name varchar (20) NOT NULL,'
                    'position varchar (30) NOT NULL, '
                    'salary integer);')
cur.execute('insert into employees (name, position, salary)' 
            'values(%s, %s, %s)',
            ("John Lebron", "junior python developer", 2000)
            )
cur.execute('insert into employees (name, position, salary)' 
            'values(%s, %s, %s)',
            ("Inesa", "loshped", 2000)
            )
conn.commit()
cur.close()
conn.close()