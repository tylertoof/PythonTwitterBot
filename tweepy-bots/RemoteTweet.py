"""
# key = LYD1qYnB7U5MGx9SoG360tdto
# key_secret = Vc8kp9pKbNRwwffy8A9Sr8tOhcsipQASY6i5D7OmDSJHWfXo7e
# bearer_token = AAAAAAAAAAAAAAAAAAAAACyxVgEAAAAAsiED71aKp98UdBMEyHKeWdAS32Y%3D5y7Xb9VgL87RmV2J1fHri33Vgeh78daXPlvxMvDqhQ2K2xqGzW
# access_token = 1458140835548041218-7qzOWAcs98BnvU91kjePOPQ8lpGT2t
# access_token_secret = owgVts7ElWeLSY16ZE2xXZlVSN9QRPkF4f46Gth0Ud4U6
"""

#import dependencies
import tweepy
import tkinter as tkin
import os.path as ospath

# variables for accessing twitter API
consumer_key = 'LYD1qYnB7U5MGx9SoG360tdto'
consumer_key_secret = 'Vc8kp9pKbNRwwffy8A9Sr8tOhcsipQASY6i5D7OmDSJHWfXo7e'
access_token = '1458140835548041218-7qzOWAcs98BnvU91kjePOPQ8lpGT2t'
access_token_secret = 'owgVts7ElWeLSY16ZE2xXZlVSN9QRPkF4f46Gth0Ud4U6'

# authenticating
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Send tweet
def twitter_post():
    tweet = text_input.get()
    print(tweet)
    # api.update_status(tweet)

# Send tweet w/media
def tweet_media_post():
    tweet = text_input.get()
    media_path = text_media_path.get()
    print(tweet)
    print(media_path)
    media_check = ospath.exists(media_path)
    print(media_check)
    if media_check == 'True':
        api.update_status_with_media(tweet, media_path)
    else:
        print('File path does not exist. Tweet not sent.')


'''Gui Stuffs'''
window = tkin.Tk()
window.title('Remote Tweet')

'''Buttons'''
# tweet
tweet_button = tkin.Button(window, text='Tweet', command=twitter_post)
tweet_button.place(x=120, y=220)

# tweet w/media
tweet_media_button = tkin.Button(window, text='Tweet & Media', command=tweet_media_post)
tweet_media_button.place(x=190, y=220)

'''text entries'''
# tweet
text_input = tkin.Entry(window, width = 30)
text_input.place(x = 100, y = 130)

# tweet w/media
text_media_path = tkin.Entry(window, width = 30)
text_media_path.place(x = 100, y = 180)

'''Gui Other'''
window.geometry('400x300')

'''End'''
window.mainloop()