#!/usr/bin/env python
import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r1=redis.Redis(connection_pool=pool)
print 'Redis size:', r1.dbsize()

for i in range(30):
    r=redis.Redis(connection_pool=pool)
    print r.mget('SuccessDownCnt', "SuccessTaskDownloadUrlCnt")
    time.sleep(1)
