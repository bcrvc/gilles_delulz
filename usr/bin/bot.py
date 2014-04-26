#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys 
 
argfile = str(sys.argv[1])
 
# API connect: 
CONSUMER_KEY = 'secret'
CONSUMER_SECRET = 'secret'
ACCESS_KEY = 'secret'
ACCESS_SECRET = 'secret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
# open txt file and read lines
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
        # get Twitter trends data and extract top trending hashtag
	trends1 = api.trends_place(1)
	print trends1
	hashtags = [x['name'] for x in trends1[0]['trends'] if x['name'].startswith('#')]
	# print hashtags
	# print hashtags[0]
        print hashtags[0]
        trend_hashtag = hashtags[0]
        api.update_status(line + ' ' + trend_hashtag)
        # Tweet every xx min ...
        time.sleep(10800)
