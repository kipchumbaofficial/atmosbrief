#!/usr/bin/env python3
"""atmosbrief
    - X bot for posting weather briefs of random cities around the world
"""
import os
import requests
import tweepy
from countryflag import getflag


# X API credentials
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Weather API credientials
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_URL = "http://api.weatherapi.com/v1/forecast.json?key={}&q={}"

# Selected Cities
african_cities = ['Accra', 'Cairo', 'Johannesburg',
                  'Kinshasa', 'Addis Ababa', 'Casablanca',
                  'Lagos', 'Abidjan', 'Dodoma', 'Nairobi']

other_cities = ['London', 'New York', 'Sydney', 'Tokyo',
                'Paris', 'Buenos aires', 'Dubai']

# Authenticate with X
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)
# for media upload
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)


# Fetch Weather data
def fetch_weather(city):
    """fetch_weather:
        - Fetches weather data from weatherapi.com for given city
        Returns:
            The weather data or None if data cant be fetched
    """
    try:
        response = requests.get(WEATHER_URL.format(WEATHER_API_KEY, city))
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve weather data")
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None


# Get sunrise in given city
def get_sunrise(city):
    """get_sunrise:
        - Get sunrise time from weather API forecast
        Returns:
            sunrise time as forecasted by weatherapi
    """
    data = fetch_weather(city)
    if data:
        return data['forecast']['forecastday'][0]['astro']['sunrise']
    else:
        return None


# Abbreviate Country name to fit tweet:
def abbreviate_country(country):
    """abbreviate_country:
        - Abbriates some chosen countries
        Returns:
            Country's abbreviation
    """
    country_abbreviations = {
        'United States of America': 'U.S.A',
        'Democratic Republic of Congo': 'D.R.C',
        "Cote d'Ivoire": 'Ivory Coast'
    }
    return country_abbreviations.get(country, country)


# Format forecast post
def create_forecast_post(city):
    """create_forecast_post:
        - Fetches the forecas data for a given city from weatherAPI
        Returns:
            Formated tweet with the days weather forecast
    """
    data = fetch_weather(city)
    if data:
        location = data['location']
        forecast_day = data['forecast']['forecastday'][0]['day']
        astro = data['forecast']['forecastday'][0]['astro']

        # Format tweet
        country = abbreviate_country(location['country'])
        forecast = (f"Today's weather forecast for {location['name']},"
                    f" {country}:\n"
                    f"- Condition: {forecast_day['condition']['text']} \n"
                    f"- High: {forecast_day['maxtemp_c']}°C, Low: "
                    f"{forecast_day['mintemp_c']}°C 🌡️\n"
                    "- Chance of Rain: "
                    f"{forecast_day['daily_chance_of_rain']}% 🌧️\n"
                    f"- Wind: {forecast_day['maxwind_kph']} km/h 🌬️\n"
                    f"- Humidity: {forecast_day['avghumidity']}% 💧\n"
                    f"- Sunrise: {astro['sunrise']} 🌞, "
                    f"Sunset: {astro['sunset']} 🌇\n"
                    f"#WeatherBriefs #{location['name'].replace(' ', '')}"
                    "Weather #StayWeatherReady")
        return forecast
    else:
        return None


# Format a post
def create_post(city):
    """create_post:
        - Formats a post before posting on x
        Returns:
            The formated tweet or None if fetching weather data fails
    """
    data = fetch_weather(city)
    if data:
        location = data.get('location')
        current = data.get('current')
        forecast_day = data['forecast']['forecastday'][0]['day']

        # Compose the tweet with required fields
        post = (f"Current weather in {location['name']}, "
                f"{location['country']} "
                f"{getflag([location['country']])}:\n"
                f"Condition: {current['condition']['text']}\n"
                f"Temperature: {current['temp_c']}°C\n"
                f"Feels Like: {current['feelslike_c']}°C\n"
                f"Last Updated: {current['last_updated']}\n"
                f"Local Time: {location['localtime']}\n"
                "- Chance of Rain: "
                f"{forecast_day['daily_chance_of_rain']}% 🌧️\n"
                f"#WeatherBriefs #{location['name'].replace(' ', '')}"
                "Weather #StayWeatherReady")

        return post
    else:
        return None
