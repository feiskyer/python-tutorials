#!/usr/bin/python
import sqlite3
 
db=sqlite3.connect('test.db')
cu=db.cursor()

cu.execute('create table catalog (id integer primary key,pid integer,name varchar(10) unique)')
cu.execute("insert into catalog values(0, 0, 'name1')")
cu.execute("insert into catalog values(1, 1, 'name2')")
db.commit() 

cu.execute('select * from catalog')
print cu.fetchall()

cu.close()
db.close() 

