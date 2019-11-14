from Twitter_key import *
import tweepy


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name=screen_name, count=280)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    print("Loading {} tweets ".format(screen_name), end=' ')
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print('.', end=' ')

    outtweets = [str(tweet.text.encode("utf-8")) for tweet in alltweets]

    return outtweets


def fit(user_account):
    return get_all_tweets(user_account)
