#!/usr/bin/env python
#coding=utf8
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import Tag,NavigableString
from urlparse import urlparse
import urllib2
import sys

def affect(points, keep_ratio, ratio, power):
    keep = points * keep_ratio
    if ratio >= 1.: return points
    return keep + (points - keep) * pow(ratio, power)

def calc_link_points(host, ul):
    # simplified host 不要子域名部分！
    parts = host.split('.')
    if parts[-2] in ('com','edu','net','gov','org'):
        host = '.'.join(host.split('.')[-3:])
    else:
        host = '.'.join(host.split('.')[-2:])
    
    link_density = linktext_count = totaltext_count = 0.001
    container_count = innerlink_count = 0.001
    for a in ul.findAll('a'):
        href = a.get('href', '')
        print href
        # 内部链接
        if not href or not href.lower().startswith('http') or host in href:
            innerlink_count += 1
            continue
        # 层次太深
        if urlparse(href)[2].strip('/').count('/') >= 1 or '?' in href:
            continue
        link_density += 1
        linktext_count += len(a.text)
        if '_blank' == a.get('target'):
            link_density += 1
    # 统计容器字数
    for t in ul.recursiveChildGenerator():
        if type(t) is NavigableString:
            totaltext_count += len(t)
        else:
            container_count += 1
    points = (link_density - innerlink_count) * 1000
    if points < 0: return 0
    
    points = affect(points, 0.1, linktext_count / totaltext_count, 2.)
    points = affect(points, 0.1, link_density / container_count, 1.)
    
    # if points < 1000: points = 0
    return points
    
def find_abstract(body):
    candidates = []
    total_links = len(body.findAll('a')) + 0.001
    # 枚举文字容器
    for tag in ('div', 'section', 'article', 'td', 'li', 'dd', 'dt', 'postbody', 'p'):
        for x in body.findAll(tag):
            if type(x) is not Tag: continue
            points = len(x.text[:100].encode('utf8')) * 1000
            points = affect(points, 0.1, 1 - len(x.findAll('a')) * 1. / total_links, 1.)
            candidates.append((points, x))
    # 排序，取分数最高的容器
    candidates.sort(reverse = True)
    if candidates:
        return candidates[0][1]
    return body
    
if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit(-1)
    html=urllib2.urlopen(sys.argv[1]).read()
    print find_abstract(BeautifulSoup(html)).text
