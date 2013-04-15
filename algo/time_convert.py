#!/usr/bin/env python
#coding=utf8

import time


#将"2011-09-28 10:00:00"转化为时间戳
a = "2011-09-28 10:00:00"
print time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))

#将时间戳转化为localtime
x = time.localtime(1317091800.0)
print time.strftime('%Y-%m-%d %H:%M:%S',x)
