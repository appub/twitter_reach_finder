# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:47:29 2017
@author: Appu B
"""

import pandas as pd 

class Parser(object):
    """ process the tweets for analysis """
    
    def __init__(self,tweets):
        self.tweets = tweets
    
    def parse(self):
        """
        Process the json formatted data and returns a pandas 
        DataFrame object with the relevent informations
        @param:tweets: list of dictionaries containing tweet info
        """   
        tweet_time = list()
        screen_name = list()
        name = list()
        text = list()
        fcount = list()
        rtcount = list()
        followers = list()
        lang = list()
        print("started processing")
        try:
            for tweet in self.tweets:
                tweet_time.append(tweet["created_at"])
                screen_name.append(tweet["user"]["screen_name"])
                name.append(tweet["user"]["name"])
                text.append(tweet["text"])
                fcount.append(tweet["favorite_count"])
                rtcount.append(tweet["retweet_count"])
                followers.append(tweet["user"]["followers_count"])
                lang.append(["lang"])
                #if "retweeted_status" in tweet.keys():
                 #   tweet_time.append(tweet["retweeted_status"]["created_at"])
                 #  screen_name.append(tweet["retweeted_status"]["user"]["screen_name"])
                 #   name.append(tweet["retweeted_status"]["user"]["name"])
                #    text.append(tweet["retweeted_status"]["text"])
                 #   fcount.append(tweet["retweeted_status"]["favorite_count"])
                  #  rtcount.append(tweet["retweeted_status"]["retweet_count"])
                   # followers.append(tweet["retweeted_status"]["user"]["followers_count"])
                    #lang.append(tweet["retweeted_status"]["lang"])
            
            data = {'created_at':pd.to_datetime(pd.Series(tweet_time)),'name':name,
                    'screen_name':screen_name,'followers':followers,
                    'tweet':text,'RTcount':rtcount,'favorite_count':fcount,'lang':lang}
            tweetTable = pd.DataFrame(data)
            return tweetTable  
        except Exception as e:
            print("Processing error: ",e)
            