# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:47:45 2017

@author: Appu B
"""
import re
import pandas as pd
from textblob import TextBlob
#from pandas.tseries.resample import TimeGrouper
#from pandas.tseries.offsets import DateOffset

class Analyser(object):
    
    def __init__(self,data):
        self.data = data
        
    def calc_reach(self):
        """
        Return the total number of accounts reached
        """
        try:
            data = self.data[['name','followers']].copy()
            # remove duplicates
            data = data.drop_duplicates()
            # return the sum of total followers count
            return sum(data['followers'])
        except Exception as e:
            print("Something happened while calculating the reach : ",e)    
    
    def popular_tweets(self, n = 5):
        """
        Returns most popular tweets 
        @param:n: number of results needed, default 5
        """
        try:
            data = self.data[['name','followers','tweet']].copy()
            # drop duplicates if any
            data = data.drop_duplicates()
            #sort tweets by follower count
            data = data.sort_values(by = 'followers', ascending=False)
            #return sorted data
            return pd.DataFrame.head(data,n)  
        except Exception as e:
            print("Something happened while retrieving the popular tweets: ",e)    
            
            
    def most_RT(self, n = 5):
        """
        Returns most retweeted tweets from the given data
        @param:n: number of results needed default 5
        
        """
        try:
            data = self.data[['name','RTcount','tweet']].copy()
            # remove retweets and retrieve original tweets by matching RT @ start of tweet
            og_tweets = data[data["tweet"].apply(lambda x : x[:2]!='RT')]
            # drop duplicates if any
            og_tweets = og_tweets.drop_duplicates()
            #sort by RTcount
            og_tweets = og_tweets.sort_values(by = 'RTcount', ascending=False)
            #return 
            return pd.DataFrame.head(og_tweets,n)
        except Exception as e:
            print("Something happened while retrieving the most RTed tweets: ",e)
    
    def get_sentiment(self):
        def senti(tweet):
            tweet = tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])\
                                    |(\w+:\/\/\S+)", " ", tweet).split()) 
            analysis = TextBlob(tweet)
            senti =''
            if analysis.sentiment.polarity > 0:
                senti = 'positive'
            elif analysis.sentiment.polarity == 0:
                senti = 'neutral'
            else:
                senti = 'negative'
            return senti
         
        data = self.data['tweet'].copy()
        data['sentiment'] = data.apply(lambda x:senti(x))
        return data 
        
    def most_favorited(self, n = 5):
        """
        Returns most favorited tweets from the given data
        @param:n: number of results needed default 5
        
        """
        try:
            data = self.data[['name','favorite_count','tweet']].copy()
            # drop duplicates if any
            og_tweets = data.drop_duplicates()
            #sort by RTcount
            og_tweets = og_tweets.sort_values(by = 'favorite_count', ascending=False)
            #return 
            return pd.DataFrame.head(og_tweets,n)
        except Exception as e:
            print("Something happened while retrieving the most favorited tweets: ",e)

    def time_series(self):
        data = self.data[['created_at']].copy()
        data['count'] = 1
        
        data.index = pd.to_datetime(data['created_at'])
        data =  data.resample('10T').apply(sum).dropna()
        
        return  data  
                 
