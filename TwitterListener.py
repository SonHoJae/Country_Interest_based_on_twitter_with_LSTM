from tweepy import StreamListener
from tweepy import Stream
import tweepy
import json
import pprint
import googletrans

class TwitterListener(StreamListener):
    global i
    def __init__(self, country_list):
        self.translator = googletrans.Translator()
        self.interest_dictionary = dict()
        self.country_list = country_list
        #print(country_list)
    def on_data(self, data):
        tweet = json.loads(data)
        # except for retweet
        if 'text' in tweet and 'RT' not in tweet['text'][:3]:
            print(tweet['lang'])

    def on_error(self, status):
        print('error occured!!')
        print(status)

