import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import seaborn as sns
import re

consumer_key = "G3GrZyg7r89FCH96iurckOhlG"
consumer_secret = "KhqhetHDZwnunqI99XqsOtfRyJv0zmHXfY5SPDdgVx6jHkZKSJ"
access_token = "2963085141-SpdCreIunpWRqcDryBAyrykEYOiX1jMHHeGoMMT"
access_token_secret = "DUcW6OJJJgO8pmZO1r9XFeSYvEeBIafJKUmkPMM5a6A2I"

# Method to get the tweets
def get_tweets(username):
    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get tweets
    tweets = api.user_timeline(screen_name=username, count=200)

    # Create a dataframe
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

    # Clean the text
    df['Tweets'] = df['Tweets'].apply(lambda x: ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x).split()))

    # Get the polarity of the tweet
    df['polarity'] = df['Tweets'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Get the subjectivity of the tweet
    df['subjectivity'] = df['Tweets'].apply(lambda x: TextBlob(x).sentiment.subjectivity)

    # Get the length of the tweet
    df['length'] = df['Tweets'].apply(lambda x: len(x))

    # Get the number of followers
    df['followers'] = df['Tweets'].apply(lambda x: x.user.followers_count)

    # Get the number of friends
    df['friends'] = df['Tweets'].apply(lambda x: x.user.friends_count)

    # Get the number of tweets
    df['tweets'] = df['Tweets'].apply(lambda x: x.user.statuses_count)

    # Get the number of likes
    df['likes'] = df['Tweets'].apply(lambda x: x.user.favourites_count)

    # Get the number of retweets
    df['retweets'] = df['Tweets'].apply(lambda x: x.retweet_count)

    # Get the number of replies