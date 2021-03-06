from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='Cioran').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        print (tweet)
        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Follow the user who tweeted
        tweet.user.follow()
        print('Followed the user')

        sleep(15)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break