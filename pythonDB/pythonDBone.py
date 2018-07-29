# sqlite database in pythoe

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('pythonDbOne.db')
# The cursor class. Allows Python code to execute PostgreSQL command in a database session
#Cursors are created by the connection.cursor() method:
#they are bound to the connection for the entire lifetime and all the commands are executed in the
#context of the database session wrapped by the connection.
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS firstDB(unix REAL, datestamp TEXT,keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO firstDB VALUES(123421389, '2016-01-02', 'ruby',8)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO firstDB (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
            (unix, date, keyword, value))
    conn.commit()




#create_table()
#data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

c.close()
conn.close()
