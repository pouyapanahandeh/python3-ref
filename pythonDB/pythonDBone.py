# sqlite database in pythoe

import sqlite3

conn = sqlite3.connect('pythonDbOne.db')
# The cursor class. Allows Python code to execute PostgreSQL command in a database session
#Cursors are created by the connection.cursor() method:
#they are bound to the connection for the entire lifetime and all the commands are executed in the
#context of the database session wrapped by the connection.
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS firstDB(unix REAL, datestamp TEXT,keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO firstDB VALUES(123456789, '2016-01-01', 'python',5)")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()
