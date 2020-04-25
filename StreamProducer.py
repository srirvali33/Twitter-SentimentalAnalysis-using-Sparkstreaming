from kafka import KafkaProducer
import kafka
import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


# API CONFIGURATIONS FROM TWITTER
consumer_key = "H6ZuqUGanFKDsJSxvJE1RHJJf"
consumer_secret = "dCqIRdpxXWH7cjTaFzy0OCiDmekc1A3uxZn7QLhHX5MT0oe4pE"
access_token = "1251001399640559616-vY3pw0z4kN1EXgD5TL8Ae2Uy6ZKXZL"
access_secret = "oqalnHSAdcCg2XlJcknIyU1Zdu7PVmfD4S4eHyaPW9Omg"

# TWITTER AUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    # Get Producer that has topic name is Twitter
    # self.producer = self.client.topics[bytes("twitter")].get_producer()

    def on_data(self, data):
        self.producer.send("twitter", data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True



twitter_stream = Stream(auth, KafkaPushListener())

# Produce Data that has tweets with the trump related hashtags
twitter_stream.filter(track=['#trump'])