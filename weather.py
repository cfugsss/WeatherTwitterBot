import requests

# Setting up API from open weather to get weather data for different cities

apiKey = "8775bf099e83fd6c1987f58bc9b257a8"
baseUrl = "http://api.openweathermap.org/data/2.5/weather"


# Creating a function for each city I want the bot to tweet updates for, also formatting the tweet in return

def weatherAC():
    requestUrl = f"{baseUrl}?appid={apiKey}&q=Atlantic City"
    responce = requests.get(requestUrl)
    data = responce.json()
    weather = data['weather'][0]['description']
    tempC = round(data['main']['temp'] - 273.15, 1)
    tempF = round(tempC * 9/5 + 32, 1)
    return(f"--Atlantic City Weather--                                                                                    Condition: {weather}                                                                             Temperature: {tempF} Fahrenheit")
     

def weatherTR():
    requestUrl = f"{baseUrl}?appid={apiKey}&q=Toms River"
    responce = requests.get(requestUrl)
    data = responce.json()
    weather = data['weather'][0]['description']
    tempC = round(data['main']['temp'] - 273.15, 1)
    tempF = round(tempC * 9/5 + 32, 1)
    return(f"--Toms River Weather--                                                                                    Condition: {weather}                                                                             Temperature: {tempF} Fahrenheit")

# def weatherVineland():
#     requestUrl = f"{baseUrl}?appid={apiKey}&q=Vineland"
#     responce = requests.get(requestUrl)
#     data = responce.json()
#     weather = data['weather'][0]['description']
#     tempC = round(data['main']['temp'] - 273.15, 1)
#     tempF = round(tempC * 9/5 + 32, 1)
#     return(f"--Vineland Weather--                                                                                    Condition: {weather}                                                                             Temperature: {tempF} Fahrenheit")

# def weatherEdison():
#     requestUrl = f"{baseUrl}?appid={apiKey}&q=Edison"
#     responce = requests.get(requestUrl)
#     data = responce.json()
#     weather = data['weather'][0]['description']
#     tempC = round(data['main']['temp'] - 273.15, 1)
#     tempF = round(tempC * 9/5 + 32, 1)
#     return(f"--Edison Weather--                                                                                    Condition: {weather}                                                                             Temperature: {tempF} Fahrenheit")
     

def weatherCH():
    requestUrl = f"{baseUrl}?appid={apiKey}&q=Cherry Hill"
    responce = requests.get(requestUrl)
    data = responce.json()
    weather = data['weather'][0]['description']
    tempC = round(data['main']['temp'] - 273.15, 1)
    tempF = round(tempC * 9/5 + 32, 1)
    return(f"--Cherry Hill Weather--                                                                                    Condition: {weather}                                                                             Temperature: {tempF} Fahrenheit")

def weatherTrenton():
    requestUrl = f"{baseUrl}?appid={apiKey}&q=Trenton"
    responce = requests.get(requestUrl)
    data = responce.json()
    weather = data['weather'][0]['description']
    tempC = round(data['main']['temp'] - 273.15, 1)
    tempF = round(tempC * 9/5 + 32, 1)
    return(f"--Trenton Weather--                                                                                    Condition: {weather}                                                                             Temperature: {tempF} Fahrenheit")

def weatherNewark():
    requestUrl = f"{baseUrl}?appid={apiKey}&q=Newark"
    responce = requests.get(requestUrl)
    data = responce.json()
    weather = data['weather'][0]['description']
    tempC = round(data['main']['temp'] - 273.15, 1)
    tempF = round(tempC * 9/5 + 32, 1)
    return(f"--Newark Weather--                                                                                    Condition: {weather}                                                                             Temperature: {tempF} Fahrenheit")


