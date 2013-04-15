#!/usr/bin/python
# coding: utf-8

# 题目日历中的年份中间被涂掉了，可以猜测年份区间为[1006, 2006]；
# 其次，进一步观察日历发现，当年的1月1日正好是周四，而且日历右下角显示的2月份有29日，因此当年应该是闰年；
# 由此计算得到几个候选的年份： [1176, 1356, 1576, 1756, 1976] 。
# 然后注意到，题目的 title 是 'whom?' 。意味着这个题目的目的应该是找一个人。 
# 在题目页面源代码上有两行提示信息：
#'he ain't the youngest, he is the second' - 据此选择年份 '1756' ；
#'todo: buy flowers for tomorrow' - 按照日历显示，当天应该是 1756年1月26日， 
# Google一下第二天（即1756年1月27日），发现是Mozart的生日！答案出来了！

import datetime

#闰年判定
def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0

candidated_years = []
for y in xrange(1006, 2007, 10):
    if datetime.date(y, 1, 1).weekday() == 3 and is_leap_year(y):
        candidated_years.append(y)

print candidated_years