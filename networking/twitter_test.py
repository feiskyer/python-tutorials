#!/usr/bin/env python
#import urllib2
#import os
#proxy_server = urllib2.ProxyHandler({'http': '127.0.0.1:8087', 'https': '127.0.0.1:8087'})
#new_opener = urllib2.build_opener(proxy_server)
#urllib2.install_opener(new_opener) 

import sys
import tweepy


CONSUMER_KEY = 'CcnXdTeMCeDW2ml5gTUw'
CONSUMER_SECRET = 'pRgX9SBKFhHPAyswYt8EL9dTTizhaSPtLU2pRGGjN0M'
ACCESS_KEY = '15938080-fVeYpUPloVvos8LIuuRO2YoGfEReoMXVwa8cuAtUo'
ACCESS_SECRET = 'Ze3bWWzsgb3NnkZKOcYZqfUBeOCx5dN78HKaNjY2nA'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#api.update_status(sys.argv[1])
user = api.get_user('twitterapi')
print user.name, ': ', user.status.text
