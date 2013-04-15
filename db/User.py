#!/usr/bin/python
from sqlalchemy.ext.declarative import *
from sqlalchemy import *

Base = declarative_base()

class User(Base):
	__tablename__='users'
	
	id = Column(Integer,primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __init__(self,name,fullname,password):
		self.name = name
		self.fullname = fullname
		self.password = password

	def __repr__(self):
		return "%s(%r,%r)"%(self.__class__.__name__,self.name,self.password)

if __name__=='__main__':
    print User.__tablename__
