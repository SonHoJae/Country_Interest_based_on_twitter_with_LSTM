# This program is with python 3.5
from tweepy import StreamListener
import json
import googletrans
import threading
import datetime

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

    # timer
    def on_connect(self):
        def funcTimer(duration):
            print(str(datetime.datetime.now()))
            timer = threading.Timer(duration, funcTimer, args=(duration,))
            timer.start()
            print(self.target_language + ' users are showing interests on \n'+googletrans.Translator().translate(str(
                                         self.interest_dictionary)).text)
            # timer.cancel()
        duration = 60
        print('Duration -> ' + str(duration) + ' seconds')
        funcTimer(duration)

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

