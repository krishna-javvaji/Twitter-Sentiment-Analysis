import tweepy
from textblob import TextBlob

# Authenticate with Twitter API
consumer_key = "CONSUMER KEY"
consumer_secret = "SECRET KEY"

access_token = "ACCESS TOKEN"
access_token_secret = "TOKEN SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search for tweets that contain the required keyword 
public_tweets = api.search_tweets(q="Your Search keyword")

# Perform sentiment analysis on each tweet
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
