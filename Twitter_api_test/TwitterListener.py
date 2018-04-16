# -*- coding:utf-8 -*-
from tweepy import StreamListener
import json
import googletrans
import threading
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode

analyzer = SentimentIntensityAnalyzer()

class TwitterListener(StreamListener):
    # timer
    # Counting country
    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                      (time_ms, tweet, sentiment))
            conn.commit()
        except KeyError as e:
            print(str(e))
        return True
    #Error handling
    def on_error(self, status):
        print('error occured!!')
        print(status)

