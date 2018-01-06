# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:05:34 2017

@author: Appu B
"""
import tweepy
import sys
import jsonpickle

class Agent():
    
    def __init__(self,ckey,csecret):
        self.ckey = ckey
        self.csecret = csecret
        self.api = None
        
    def set_keys(self):
        # Replace the API_KEY and API_SECRET with your key and secret.
        auth = tweepy.AppAuthHandler(consumer_key = self.ckey, 
                                     consumer_secret = self.csecret)
        # Create an api with auth
        self.api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)
        # check  for authentication
        if (not self.api):
            print ("Can't Authenticate")
            sys.exit(-1)


    def search(self,query,ntweets):
        """
        Returns a list of dictionaries containing searched tweets
        @param:query: the keyword for which twitter timeline is scanned
        @param:ntweets: number of tweets to be searched for  
        """
        tweetsPerQry = 100
        tweetCount = 0
        sinceId = None
        full_tweets = list()
        max_id = -1
        # using max_id and since_id to avoid recieving duplicates
        # while searching
        #moreinfo @ https://dev.twitter.com/rest/public/timelines
        while tweetCount< ntweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = self.api.search(q=query, lang = 'en',count=tweetsPerQry)
                    else:
                        new_tweets = self.api.search(q=query, lang = 'en',count=tweetsPerQry,
                                                    since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = self.api.search(q=query, lang = 'en',count=tweetsPerQry,
                                                            max_id=str(max_id - 1))
                    else:
                        new_tweets = self.api.search(q=query,lang = 'en', count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
                
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    full_tweets.append(tweet._json)
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break
        return full_tweets  



def save_to_file(fname,tweets):
    with open(fname,'w',encoding = 'utf-8') as f:
        for tweet in tweets:
              f.write(jsonpickle.encode(tweet, unpicklable=False) +'\n')
