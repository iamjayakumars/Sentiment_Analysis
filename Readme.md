This is a python program to analyse sentiments from public tweets using textblob package in python.
The program analyses the sentiments with a polarity threshold of negative values, zero and positive values for negative, neutral and positive sentiment respectively.
Once it has analysed the sentiments, it writes the data to a csv file with the tweets and their respective sentiments.

You'll need to create a new app on apps.twitter.com to get the access token and consumer key.

The program uses the following packages:
  * **textblob** to analyse the polarity of tweet
  * **tweepy** to use the twitter API
  * **numpy** for other operations
