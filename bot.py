import weather
import tweepy

# You can put keys here for import them from a seperate text file

API_KEY = "KEY HERE"
API_KEY_SECRET = "KEY HERE"
BEARER_TOKEN = "KEY HERE"
ACCESS_TOKEN = "KEY HERE"
ACCESS_TOKEN_SECRET = "KEY HERE"

# Setting up twitter API

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Creating loop to tweet updates for each city
# Server uses seperate scheduling to run code at certain times

run = True

while run:
    try:
        api.update_status(weather.weatherAC())
        api.update_status(weather.weatherTR())
        api.update_status(weather.weatherCH())
        api.update_status(weather.weatherTrenton())
        api.update_status(weather.weatherNewark())
        run = False
    except:
        print("failed")
        run = False




    