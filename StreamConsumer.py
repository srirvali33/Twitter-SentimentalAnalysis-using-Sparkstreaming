from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch
from textblob import TextBlob
es = Elasticsearch()
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():
    '''
    main function initiates a kafka consumer, initialize the tweetdata database.
    Consumer consumes tweets from producer extracts features, cleanses the tweet text,
    calculates sentiments and loads the data into postgres database
    '''
    # set-up a Kafka consumer
    consumer = KafkaConsumer("twitter")
    for msg in consumer:

        dict_data = json.loads(msg.value)
        sA = SentimentIntensityAnalyzer()

        tweet = TextBlob(dict_data["text"])
        polarity = sA.polarity_scores(tweet)
        if (polarity["compound"] > 0):
            dict_data["created_at"]= "positive"
        elif (polarity["compound"] < 0):
            dict_data["created_at"]=  "negative"
        else:
            dict_data["created_at"]=  "neutral"
        print(tweet+" - has "+ dict_data["created_at"] + " sentiment")

        # adding the  text and sentiment info accordingly to elasticsearch
        es.index(index="tweet",
                  doc_type="test-type",
                  body={"author": dict_data["user"]["screen_name"],
                        "Positivity": dict_data["created_at"],
                        "message": dict_data["text"]})
        print('\n')

if __name__ == "__main__":
    main()
