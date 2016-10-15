import tweepy
from textblob import TextBlob
import numpy as np

consumer_key = ''   #enter consumer_key here in quotes
consumer_secret = ''    #enter consumer_secret key in quotes

access_token = ''       #enter access_token in quotes
access_token_secret = ''    #enter access_token_secret in quotes

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('sick')                  #searhing for the tweets for a search term
tweet_count = len(public_tweets)                    

senti = np.chararray((1,tweet_count), itemsize = 8)
emotion = np.empty([1, tweet_count])

for i in range (tweet_count):
    analysis = TextBlob(public_tweets[i].text)
    emotion[0, i] = analysis.sentiment.polarity         #storing polarity for tweets
    if emotion [0, i] < 0:                  #sentiment according to polarity thresholds of negative, 0 and positive values respectively
        senti[0, i] = 'negative'
    elif emotion [0, i] == 0:
        senti[0, i] ='neutral'
    else:
        senti[0, i] = 'positive'

file = open('senti_analysis.csv', 'w')

for i in range (tweet_count):
    file.write((public_tweets[i].text).encode('utf-8'))
    file.write(', ')
    file.write(str(senti[0, i]));
    file.write('\n')

file.close()
