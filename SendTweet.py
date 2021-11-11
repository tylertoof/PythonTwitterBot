import tkinter as tk
import tweepy
from keys import keys


# Authenticate to Twitter
from tweepy import API
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def sendTweet():
    tweet = entry1.get()
    api.update_status(status=tweet)
    label1 = tk.Label(root, text="Tweet sent: " + tweet)
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Send Tweet', command=sendTweet)
canvas1.create_window(200, 180, window=button1)

root.mainloop()