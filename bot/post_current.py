#!/usr/bin/env python3
"""post_current module:
    - Contains logic of posting current weather updates
    functions:
        post_current_weather - posts current weather
        post_cities_weather - Posts current weather of all cities
"""
from atmosbrief import create_post, client, african_cities


# Post on X using X API V2
def post_current_weather(city):
    """post_tweer:
        - Posts the updates on x @atmosbrief
        Returns:
            None
    """
    post = create_post(city)
    if post:
        try:
            client.create_tweet(text=post)
            print(f"Tweet posted for {city}: {post}")
        except Exception as e:
            print(f"Error posting tweet: {e}")
    else:
        print(f"No weather data for {city}")


# Post current weather for African cities
def post_cities_current():
    """post_cities_current:
        - Posts current weather of all african cities
        Returns:
            None
    """
    for city in african_cities:
        post_current_weather(city)


if __name__ == "__main__":
    post_cities_current()
