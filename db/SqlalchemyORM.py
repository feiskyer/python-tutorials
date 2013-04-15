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

Session = sessionmaker(bind = db)
session = Session()
user1 = User('name1','fullname','ps')
user2 = User('name2','fullname','ps')
user3 = User('name3','fullname','ps')
session.add(user1)
session.add(user2)
session.add(user3)
#session.flush()
session.commit()

# query by name
userlist = session.query(User).filter_by(name='name1')
for user in userlist:
	print user

# query all
userlist = session.query(User)
for user in userlist:
	print user

# update
userlist = session.query(User).filter_by(name='name1')
for user in userlist:
	user.name='user55'
	user.password='new'
session.commit()

userlist=session.query(User).filter_by(name='user55')
for user in userlist:
	print user
