#!/usr/bin/python
#-*- coding: utf-8 -*-
from tweepy import Stream
import tweepy
import TwitterListener
import sys

consumer_key = '5z0sfk6FYOa6HQwsW50o2rcTc'
consumer_secret = 'uSf6mPLhqVew9QyWsFUp8N6cUEpBDRNwrU48hRpsMrJzOId7UK'
access_token_key = '912715351355383808-ExBFy5wIibRYYuKnjGRarHtzNxXPPnG'
access_token_secret = 'p4VlHmYZwSSUNakbUVz4xU0qrqdX8Vo2EkWXMMu7jkmfR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

if __name__ == '__main__':
    target_language = sys.argv[1] # country argv
    target_language = 'japanese'
    # country list from target language
    countries = open('./countries_language/countries_'+target_language,'rt', encoding='UTF8')
    country_list = []
    country_code_dict = dict()
    for country in countries.readlines():
        country_list.append(country.strip('\n'))

    # language code information
    language_code_file = open('language_code','rt', encoding='UTF8')
    for country_code in language_code_file.readlines():
        country, code = country_code.split()
        country_code_dict[country] = code

    # twitter listener with passing country list
    twitterListener = TwitterListener.TwitterListener(target_language, country_list)
    twitterStream = Stream(auth, twitterListener)
    print('connecting..')
    print('country list ' + str(country_list))
    print('counting country ..from ' + target_language.upper())
    twitterStream.sample(languages=[country_code_dict[target_language]],async=True)

    #filtering Examples
    #twitterStream.sample(languages=languages)
    #twitterStream.filter(async=True, track=['지진'], languages=['ko'])
    print('listening..')