#!/usr/bin/python
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
from User import *

db=create_engine("sqlite:///tutorial.db")
metadata = MetaData(db)

users_table = Table('users',metadata,
		Column('id',Integer,primary_key=True),
		Column('name',String(20)),
		Column('fullname',String(20)),
		Column('password',String(20)))
metadata.create_all(db)

# insert
i=users_table.insert()
i.execute(name='Mary',password='secure')
i.execute({'name':'Tom'},{'name':'Fred'},{'name':'Harry'})

# get all data
s=users_table.select()
data=s.execute().fetchall()
for d in data:
	print d['name'],
print

# select by name
data=users_table.select(users_table.c.name=='Harry').execute().fetchall()
for d in data:
	print d['name'],d['password']
print

# update 
users_table.update().where(users_table.c.name=='Harry').values(password='$$$$$').execute()
data=users_table.select(users_table.c.name=='Harry').execute().fetchall()
for d in data:
	print d['name'],d['password']
print

# delete
users_table.delete().where(users_table.c.name=='Harry').execute()
data=users_table.select(users_table.c.name=='Harry').execute().fetchall()
if data:
	for d in data:
		print d['name'],d['password']
else:
	print 'None'
