#import dependencies
import tweepy
import sys

# variables for accessing twitter API
consumer_key = 'LYD1qYnB7U5MGx9SoG360tdto'
consumer_key_secret = 'Vc8kp9pKbNRwwffy8A9Sr8tOhcsipQASY6i5D7OmDSJHWfXo7e'
access_token = '1458140835548041218-7qzOWAcs98BnvU91kjePOPQ8lpGT2t'
access_token_secret = 'owgVts7ElWeLSY16ZE2xXZlVSN9QRPkF4f46Gth0Ud4U6'

# authenticating
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if len(sys.argv) == 2:
    # text tweet
    api.update_status(sys.argv[1])
else:
    # text & media tweet
    api.update_status_with_media(sys.argv[1], sys.argv[2])