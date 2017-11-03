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
        try:
            # except for retweet
            if 'RT' not in tweet['text'][:3] and 'text' in tweet:
                # extract country list from a tweet
                found_country = set([word for word in tweet['text'].split() if word in self.country_list])
                #print(found_country)
                #print(str(tweet['user']['screen_name']) + ' : ' + str(tweet['text']) + ' from ' + str(tweet['user']['location']))

                for country in found_country:
                    if country not in self.interest_dictionary:
                        self.interest_dictionary[country] = 1
                    else:
                        self.interest_dictionary[country] += 1
                print(self.interest_dictionary)
        except json.decoder.JSONDecodeError as jsonError:
            print('error occured!')
            print(jsonError)

    def on_error(self, status):
        print('error occured!!')
        print(status)

