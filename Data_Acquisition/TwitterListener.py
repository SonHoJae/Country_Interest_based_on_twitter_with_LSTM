# -*- coding:utf-8 -*-
from tweepy import StreamListener
import json
import googletrans
import threading
import datetime
import sqlite3

class TwitterListener(StreamListener):

    def __init__(self, target_language, country_list):
        # Google translator needs to resolve emoji issue(json error!)
        self.translator = googletrans.Translator()
        # Country : Count pair
        self.interest_dictionary = dict()
        # Country list from target language
        self.country_list = country_list
        # Target language
        self.target_language = target_language
        # log file
        self.conn = sqlite3.connect('country_count.db', check_same_thread=False)
        self.c = self.conn.cursor()

    # timer
    def on_connect(self):
        def funcTimer(duration):

            timer = threading.Timer(duration, funcTimer, args=(duration,))
            timer.start()

            time = str(datetime.datetime.now())
            result = googletrans.Translator().translate(str(self.interest_dictionary)).text
            print(str(self.interest_dictionary))
            print(time)
            insert_sql = 'INSERT INTO korean (country, count) VALUES (?,?)'
            update_sql = 'UPDATE korean SET count = ? WHERE country = ? '
            for info in self.interest_dictionary:
                print(info)
                print(self.interest_dictionary[info])
                try:
                    self.c.execute(insert_sql,(info,self.interest_dictionary[info]))
                except sqlite3.IntegrityError:
                    self.c.execute(update_sql, (self.interest_dictionary[info],info))
            self.conn.commit()

            #print(self.target_language + ' users are showing interests on \n'+result)

        duration = 5
        print('Duration -> ' + str(duration) + ' seconds')
        funcTimer(duration)
        sql = 'create table if not exists ' + 'KOREAN' + ' (Country TEXT UNIQUE, Count INTEGER NOT NULL DEFAULT 0)'
        self.c.execute(sql)


    # Counting country
    def on_data(self, data):

        tweet = json.loads(data)

        # Not Consider Retweet
        if 'text' in tweet and 'RT' not in tweet['text'][:3]:
            #TODO: Need to check korea's in korea
            found_country = set([country for word in tweet['text'].split() for country in self.country_list if country
                                 in word])
            # counting..
            for country in found_country:
                if country not in self.interest_dictionary:
                    self.interest_dictionary[country] = 1
                else:
                    self.interest_dictionary[country] += 1
                #print(self.interest_dictionary) # when updated

    # Error handling
    def on_error(self, status):
        print('error occured!!')
        print(status)

