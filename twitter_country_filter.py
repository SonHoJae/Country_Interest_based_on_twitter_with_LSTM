
from tweepy import StreamListener
from tweepy import Stream
import tweepy
import TwitterListener
import json
import threading

consumer_key = '5z0sfk6FYOa6HQwsW50o2rcTc'
consumer_secret = 'uSf6mPLhqVew9QyWsFUp8N6cUEpBDRNwrU48hRpsMrJzOId7UK'
access_token_key = '912715351355383808-ExBFy5wIibRYYuKnjGRarHtzNxXPPnG'
access_token_secret = 'p4VlHmYZwSSUNakbUVz4xU0qrqdX8Vo2EkWXMMu7jkmfR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

if __name__ == '__main__':

    countries = open('./countries_language/countries_english','rt', encoding='UTF8')
    country_list = []
    for country in countries.readlines():
        country_list.append(country.strip('\n'))
    language_code_file = open('language_code','rt', encoding='UTF8')
    languages = [country_code.split()[1] for country_code in language_code_file.readlines()]
    print(languages)
    twitterListener = TwitterListener.TwitterListener(country_list)
    twitterStream = Stream(auth, twitterListener)
    print('connecting..')
    twitterStream.sample()
    #twitterStream.filter(async=True, track=['지진'], languages=['ko'])
    print('listening..')