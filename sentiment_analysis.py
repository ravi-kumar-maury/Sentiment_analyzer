import tweepy
import Textblob as t
consumer_key='*******************'
consumer_secret='****************'
access_token='**************'
access_token_secret='************'  # am not showing my access token,secret here 
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
public_tweets=api.search('Computer')
for tweet in public_tweets:
   print(tweet.text)
   analysis=TextBlob(tweet.text)
   print(analysis)
