from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch
from textblob import TextBlob
es = Elasticsearch()
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():
    
    # setting up the Kafka consumer
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

        # add text and sentiment info to elasticsearch
        es.index(index="tweet",
                  doc_type="test-type",
                  body={"author": dict_data["user"]["screen_name"],
                        "Positivit": dict_data["created_at"],
                        "message": dict_data["text"]})
        print('\n')

if __name__ == "__main__":
    main()
