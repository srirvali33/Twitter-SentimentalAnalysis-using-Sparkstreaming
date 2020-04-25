from kafka import KafkaProducer
import kafka
import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# TWITTER CONFIGURATIONS
consumer_key = "H6ZuqUGanFKDsJSxvJE1RHJJf"
consumer_secret = "dCqIRdpxXWH7cjTaFzy0OCiDmekc1A3uxZn7QLhHX5MT0oe4pE"
access_token = "1251001399640559616-vY3pw0z4kN1EXgD5TL8Ae2Uy6ZKXZL"
access_secret = "oqalnHSAdcCg2XlJcknIyU1Zdu7PVmfD4S4eHyaPW9Omg"

# TWITTER AUTHENTICATION
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    
    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        self.producer.send("twitter", data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True


# Twitter Stream Config
twitter_stream = Stream(auth, KafkaPushListener())

# Produce Data that has trump hashtag (Tweets)
twitter_stream.filter(track=['#corona'])