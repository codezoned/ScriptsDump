#Written by Senthil @Rats12
import tweepy
from textblob import TextBlob 

consumer_key = ''
consumer_secret = ''

labels = []
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)


def rtweet():
    public_tweets = api.search('string')

        #needs error handling (cant retweet if already rted)
    for tweet in public_tweets:
        print (tweet.id)
        text=TextBlob(tweet.text)
        print(text)
        api.retweet(tweet.id)


def deleteall():
    tweets=api.user_timeline() #gathers all tweets from authenticated uesr
    for tweet in tweets:
        api.destroy_status(tweet.id)


#rtweet()
#deleteall()



