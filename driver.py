# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:32:12 2017

@author: Appu B
"""
import twitteragent
import keys
from tweetparser import Parser
import analyser

agent = twitteragent.Agent(keys.ckey,keys.csecret)
agent.set_keys()
tweets = agent.search("linux",300)
processed_tweets = Parser(tweets).parse()
ar = analyser.Analyser(processed_tweets)
reach = ar.calc_reach()
x = str(max((processed_tweets['created_at'])))
y = str(min((processed_tweets['created_at'])))
print("Aanalyzed tweets from %s to %s :"%(y,x))
print("The number of accounts reached :",reach)
print("***************************************")
populartweets = ar.popular_tweets()
print("The most popular tweets")
print(populartweets)
mostRT = ar.most_RT()
print("most rt")
print(mostRT)
mostFV = ar.most_favorited() 
print("most favorited")
print(mostFV)
time_series = ar.time_series()
print("time_series")
print(time_series)
senti = ar.get_sentiment()