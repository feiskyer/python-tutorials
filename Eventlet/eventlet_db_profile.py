#!/usr/bin/env python
import eventlet
import time
import random
import MySQLdb
import eventlet.db_pool as db_pool
from DBUtils.PooledDB import PooledDB

conn_kwargs={'host':'10.241.226.41', 'user':'root', 'passwd':'feisky','db':'news', 'charset': 'utf8'}
sql="""select * from news limit 1"""
pooled=db_pool.ConnectionPool(MySQLdb, **conn_kwargs)
pooldb=PooledDB(MySQLdb, **conn_kwargs)

def query(conn):
    cur=conn.cursor()
    #cur.execute(sql % (random.randint(1,1000)))
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    return data

def test_mysqldb(times):
    now = time.time()
    for i in range(times):
        conn=MySQLdb.connect(**conn_kwargs)
        r=query(conn)
        print r
        conn.close()
    print 'MySQLdb: ', time.time()-now

def test_eventlet(times):
    now = time.time()
    for i in range(times):
        conn=pooled.get()
        try:
            r=query(conn)
            print r
        finally:
            pooled.put(conn)
    print 'Eventlet: ', time.time()-now

def test_dbutils(times):
    now = time.time()
    for i in range(times):
        conn=pooldb.connection()
        try:
            r=query(conn)
            print r
        finally:
            conn.close()
    print 'DBUtils: ', time.time()-now

#test_mysqldb(10000)            # 50s
#test_eventlet(10000)            # 31s
test_dbutils(10000)            # 30s
