#!/usr/bin/python3
# coding=utf-8

# Import Library yang dibutuhkan
import tweepy
import csv
import pandas as pd

# Masukkan Twitter Token API
consumer_key = "CzT9uAtW5U1yilFkiRdiJbCw8"
consumer_secret="hNP1znduESRlMSR1pHX8lzieqMJyS4xckgj71Ltyk2SdOWewiC"
access_token= "1202758645886283778-a0P1TrwWsnCBTzfYCUjo4RNuuXGm7o"
access_token_secret= "ugxqkum7rdf74CbRCovVY9Kls7xdg7P6KTqhTw1eHWLO4"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


# Buat path file CSV kedalam variabel
csvFile = open('dataset_covid_ina.csv', 'a')

# buat variabel baru untuk membuat file csv
csvWriter = csv.writer(csvFile)

# Mulai crawling search tweet
for tweet in tweepy.Cursor(api.search,
						   q='covid-19',
                           lang="in",
                           tweet_mode="extended").items():
    print (tweet.full_text)
    csvWriter.writerow([tweet.full_text.encode('utf-8')])