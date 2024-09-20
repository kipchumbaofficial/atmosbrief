#!/usr/bin/env python3
"""post_forecast module:
    - contains logics of how the bot post welcoming message
    and weather forecast
    functions:
        post_welcoming message - Posts salutation at sunrise in Nairobi
        post_weather_forecast - Posts Weather forecast of a given city
        post_cities_forecast - Posts Weather forecast of all the given cities
"""
from datetime import datetime
from atmosbrief import get_sunrise, api, client, other_cities
from atmosbrief import create_forecast_post, african_cities


# Post salutation
def post_welcoming_message():
    """post_welcoming_message:
        - Posts salutation before posting weather updates
        Returns:
            None
    """
    current_date = datetime.now().strftime("%B %d, %Y")
    day_of_week = datetime.now().strftime("%A")
    welcome_message = (f"Good morning! It's {day_of_week}, "
                       f"{current_date}. "
                       f"{get_sunrise('Nairobi')} "
                       "and the sun is up in Nairobi! 🌅.\n"
                       "#WeatherBriefs are on the way with "
                       "your latest updates.\n"
                       "turn on notifications 🔔 "
                       "#StayWeatherReady")
    image_path = "../images/nairobi.jpeg"

    try:
        # Upload the image and get media_id
        media = api.media_upload(image_path)

        # Post the tweet with image
        client.create_tweet(text=welcome_message,
                            media_ids=[media.media_id])
        print(welcome_message)
        print("Welcoming tweet posted.")
    except Exception as e:
        print(f"Error posting welcoming tweet: {e}")


# Post Weather Forecast
def post_weather_forecast(city):
    """post_weather_forecast:
        - Posts the weather forecast every morning
        Returns:
            None
    """
    forecast = create_forecast_post(city)
    if forecast:
        try:
            client.create_tweet(text=forecast)
            print(f"Tweet posted for {city}: {forecast}")
        except Exception as e:
            print(f"Error posting tweet: {e}")
    else:
        print(f"No weather data for {city}")


# Post Weath Forecast for all the cities
def post_cities_forecast():
    """post_cities_forecast:
        - Post forecast of all the choosen 17 cities
        Returns:
            None
    """
    post_welcoming_message()  # first tweet of the day
    all_cities = african_cities + other_cities
    for city in all_cities:
        post_weather_forecast(city)


if __name__ == "__main__":
    post_cities_forecast()
