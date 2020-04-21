import tweepy, codecs
from aylienapiclient import textapi


## fill in your Twitter credentials
consumer_key = ‘your consumer key here’
consumer_secret = ‘your consumer secret key here’
access_token = ‘your access token here’
access_token_secret = ‘your access token secret here’

## let Tweepy set up an instance of the REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## fill in your search query and store your results in a variable
results = api.search(q = "your search term here", lang = "en", result_type = "recent", count = 1000)

## use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("your text file name here.txt", "w", "utf-8")
for result in results:
    file.write(result.text)
    file.write("\n")
file.close()
