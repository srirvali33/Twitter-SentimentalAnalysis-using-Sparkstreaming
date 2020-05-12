# Twitter-SentimentalAnalysis-using-kafka-Sparkstreaming-Elasticsearch-kibana


The framework performs SENTIMENT analysis of particular hash tags in twitter data in real-time. 
For example, we want to do the sentiment analysis for all the tweets for #trump, #coronavirus.

Scrapper(tweets.py): The scrapper will collect all tweets and sends them to Kafka for analytics. The scraper will be a standalone program and will perform the followings:

 a. Collect tweets in real-time with particular hash tags. (#trump, #coronavirus)
 b. After getting tweets we will filter them to check if location field is present or not. 
 c. After filtering, we will send them (tweets) to Kafka.
 d. Kafka API (producer) is used. (https://kafka.apache.org/090/documentation.html#producerapi)
 e. Scrapper program will run infinitely and should take hash tag as input parameter while running.
Kafka: You need to install Kafka and run Kafka Server with Zookeeper. You should create a dedicated channel/topic for data transport. (https://kafka.apache.org/quickstart)

Sentiment Analyzer: Sentiment Analysis is the process of determining whether a piece of writing is positive, negative or neutral. It's also known as opinion mining, deriving the opinion or attitude of a speaker.
Sentiment analysis using Spark Streaming: In Spark Streaming, create a Kafka consumer and periodically collect filtered tweets from scrapper. For each hash tag, perform sentiment analysis using Sentiment Analyzing tool (discussed above). Then for each hash tag, send the output to Elasticsearch for visualization under kibana.

Some of results obtained for postive,negative and neutral sentimental analysis of word #coronavirus were found to be:(Shown for postive results below)


![myimage-alt-tag](https://github.com/srirvali33/Twitter-SentimentalAnalysis-using-Sparkstreaming/blob/master/coronavirus-positive.png)



After 10 min the count tends to increase from 112 to 140 as below



![myimage-alt-tag](https://github.com/srirvali33/Twitter-SentimentalAnalysis-using-Sparkstreaming/blob/master/coronavirus-positive-after10min.png)
