#!/usr/bin/env python3
'''Fetch and post weather updates for different continents'''

from atmosbrief import fetch_weather, plot_weather_table, api, client

# Dictionary with continents as keys and city lists as values
major_cities_by_continent = {
    "🌏 Asia": ["Tokyo", "Delhi", "Shanghai", "Karachi", "Dhaka"],
    "🌍 Europe": ["Moscow", "London", "Berlin", "Madrid", "Rome"],
    "🌎 North America": [
        "New York City", "Mexico City", "Toronto", "Havana", "Guatemala City"
    ],
    "🌎 South America & Oceania": [
        "São Paulo", "Buenos Aires", "Lima", "Santiago", "Sydney"
    ],
    "🌍 Africa": ["Nairobi", "Lagos", "Johannesburg", "Cairo", "Kinshasa"]
}

# Loop through each continent and its cities
for continent, cities in major_cities_by_continent.items():
    print(f"Fetching weather for {continent}...")

    # Fetch weather data
    weather_info = fetch_weather(cities)

    # Generate and save the weather table
    path = plot_weather_table(weather_info)

    # Upload the image to Twitter
    media = api.media_upload(path)

    # Post the tweet with the continent name
    client.create_tweet(
        text=f"{continent} Weather Update", media_ids=[media.media_id]
    )

    print(f"Weather Update for {continent} posted successfully!")
