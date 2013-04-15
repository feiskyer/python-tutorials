#!/usr/bin/env python
"""A simple web server that accepts POSTS containing a list of feed urls,
and returns the titles of those feeds.
"""
import eventlet
import sys
import logging
from eventlet.green import urllib

default_encoding = sys.getfilesystemencoding()
if default_encoding.lower() == 'ascii':       
    default_encoding = 'utf-8'            

# the pool provides a safety limit on our concurrency
pool = eventlet.GreenPool()
logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(name)s %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S',)
        #filename='wsgi_server.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_client_address(environ):
    try:
        return environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()
    except KeyError:
        return environ['REMOTE_ADDR']

def get_request_path(environ):
    return environ.get('PATH_INFO', '')

def get_request_params(environ):
    params={}
    param=environ.get('QUERY_STRING', '')
    if len(param)>0:
        param_list=urllib.unquote(param).split('&')
        for para in param_list:
            key,value=para.split('=')
            params[key]=value
    return params

def get_env(env):
    from pprint import pformat
    return '%s\r\n' % pformat(env)

def app(environ, start_response):
    if environ['REQUEST_METHOD'] != 'GET':
        start_response('403 Forbidden', [])
        return ['403 Forbidden']
    
    # the pile collects the result of a concurrent operation
    pile = eventlet.GreenPile(pool)
    pile.spawn(get_request_path, environ)
    pile.spawn(get_env, get_request_params(environ))
    client_ip = get_client_address(environ)
    logger.info('Client %s connected', client_ip)
    pile.spawn(get_env, environ)
    # since the pile is an iterator over the results, 
    # you can use it in all sorts of great Pythonic ways
    message = '\n'.join(pile)
    start_response('200 OK', [('Content-type', 'text/plain;charset=utf-8')])
    return [message]

if __name__ == '__main__':
    from eventlet import wsgi
    wsgi.server(eventlet.listen(('0.0.0.0', 9010)), app) #, log=file('wsgi_server_.log','a+'))
