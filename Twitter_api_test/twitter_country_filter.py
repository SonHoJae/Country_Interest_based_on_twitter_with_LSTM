#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import tweepy
from tweepy import Stream
from Twitter_api_test import TwitterListener
import sqlite3
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
    conn.commit()

create_table()

consumer_key = '5z0sfk6FYOa6HQwsW50o2rcTc'
consumer_secret = 'uSf6mPLhqVew9QyWsFUp8N6cUEpBDRNwrU48hRpsMrJzOId7UK'
access_token_key = '912715351355383808-ExBFy5wIibRYYuKnjGRarHtzNxXPPnG'
access_token_secret = 'p4VlHmYZwSSUNakbUVz4xU0qrqdX8Vo2EkWXMMu7jkmfR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)


if __name__ == '__main__':
    twitterListener = TwitterListener.TwitterListener()
    twitterStream = Stream(auth, twitterListener)
    #twitterStream.sample(languages=[country_code_dict[target_language]],async=True)

    #filtering Examples
    #twitterStream.sample(languages=languages)
    twitterStream.filter(async=True, track=['배고파'],languages=['ko'])#, languages=[
    # 'en'])
    print('listening..')