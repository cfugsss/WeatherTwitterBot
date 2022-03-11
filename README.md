# WeatherTwitterBot

This bot uses openweather API and twitter API. The Twitter account @JerseyForecast will tweet out the weather forecast/conditions at 7am everyday. The weather program handles
the openweather API and functions for getting the data for each city. The bot program initializes the twitter API using tweepy and uses a while loop to post each update.
Technically the while loop isnt needed since the server running the code has its own scheduling module; However the loop uses try and except that way incase there is a problem
retreiving the data for a city, the program will still work for other cities. 

In the future I may come back to this to add more features like replying to mentions, liking other tweets and following users. 

If youd like to use this simple bot for your own account, feel free. All you have to do is make a new twitter account (be sure to verify with phone number), apply for a 
twitter developer account, then import your keys to the bot.py program. Also be sure to apply for an elevated access acount so you have read and write permissions. You
can use free hosting like pythonanywhere.com to run your program. This site also has a scheduling feature (1 per day). Create your own functions and have your bot do
whatever you want! 
