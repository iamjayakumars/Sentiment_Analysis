import tweepy
from textblob import TextBlob
import numpy as np

consumer_key = 'RnCbEhCOKiliqX5ULgkx9R53j'
consumer_secret = 'chqbjdQQULEQC1R6GIaGhgjVvrlARswbpRlpytZ8a9BvOm3tel'

access_token = '371762066-l71iEWCkqFdoLRHd8O8Zsfbf2cPMaxgIWSjP21sw'
access_token_secret = 'wLMDNHH7HvNnEaXCebCHhgeG8GEuBaGODNjmTmXzEUIuU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('sick')
tweet_count = len(public_tweets)

senti = np.chararray((1,tweet_count), itemsize = 8)
emotion = np.empty([1, tweet_count])

for i in range (tweet_count):
    analysis = TextBlob(public_tweets[i].text)
    emotion[0, i] = analysis.sentiment.polarity
    if emotion [0, i] < 0:                  #sentiment according to polarity thresholds of negative, 0 and positive values respectively
        senti[0, i] = 'negative'
    elif emotion [0, i] == 0:
        senti[0, i] ='neutral'
    else:
        senti[0, i] = 'positive'

for i in range (len(public_tweets)):        #printing the sentiment analysis
    print public_tweets[i].text
    print senti [0, i]
    print emotion [0,i]

file = open('senti_analysis.csv', 'w')

for i in range (tweet_count):
    #file.write((str(public_tweets[i].text)+', '+str(senti[0, i])).encode('utf-8'))
    file.write((public_tweets[i].text).encode('utf-8'))
    file.write(', ')
    file.write(str(senti[0, i]));
    file.write('\n')

file.close()
