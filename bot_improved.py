#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys 

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'mzUfUYNaVFfQNJQH6eKkFA'
CONSUMER_SECRET = 'qzFwHhOmtwUtr5ZFa4e9bZyFMd2rIs2Nv5hhoNek'
ACCESS_KEY = '2443977175-2eDG1SNJ7lPtmNGlMPHSDEGa9uibrJCwI6m9rTj'
ACCESS_SECRET = 'N7WJACigY1VZnfijcl4riMWnWPpowzhbSWffveNtXHgA9'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    trends1 = api.trends_place(1)
    hashtags = [x['name'] for x in trends1[0]['trends'] if x['name'].startswith('#')]
    trend_hashtag = None
    if len(hashtags[0]) <= 20:
        trend_hashtag = hashtags[0]
    elif len(hashtags[1]) <= 20:
        trend_hashtag = hashtags[1]
    elif len(hashtags[2]) <= 20:
        trend_hashtag = hashtags[2]
    if trend_hashtag:
        api.update_status(line + trend_hashtag)
        time.sleep(3*60*60)
    else:
        time.sleep(15*60)
