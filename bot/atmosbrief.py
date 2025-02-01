#!/usr/bin/env python3
"""atmosbrief
    - X bot for posting weather briefs of Selected cities around the world
"""
import os
from datetime import datetime
import requests
import tweepy
import matplotlib.pyplot as plt
from matplotlib.table import Table


# X API credentials
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Weather API credientials
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_URL = "http://api.weatherapi.com/v1/forecast.json?key={}&q={}"

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
def fetch_weather(cities, timeout=5):
    """fetch_weather:
        - Fetches weather data from weatherapi.com for given cities
        Args:
            cities (list): A list of city names.
            timeout (int): Timeout in seconds for each request (default: 5s)
        Returns:
            list: A list of dictionaries containing processed weather data.
    """
    weather_data = []

    for city in cities:
        try:
            response = requests.get(
                WEATHER_URL.format(WEATHER_API_KEY, city), timeout=timeout
                )
            if response.status_code == 200:
                data = response.json()
                weather_info = {
                    'name': city,
                    'condition': data['current']['condition']['text'],
                    'temp': data['current']['temp_c'],
                    'daily_chance_of_rain': data[
                        'forecast']['forecastday'][0]['day'][
                        'daily_chance_of_rain'
                    ],
                    'maxwind_kph': data['forecast']['forecastday'][0]['day'][
                        'maxwind_kph'
                    ],
                    'avghumidity': data['forecast']['forecastday'][0]['day'][
                        'avghumidity'
                    ]
                }
                weather_data.append(weather_info)
            else:
                print("Failed to retrieve weather data")
        except requests.exceptions.Timeout:
            print(f"Timeout error for {city}. Skipping....")
        except requests.exceptions.RequestException:
            print(f"Error fetching weather data for {city}")

    return weather_data


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


def plot_weather_table(data):
    """
    Plots weather data as a table using Matplotlib.

    Args:
        data (list): A list of dictionaries containing weather deatils
    """
    # Extra column headers
    columns = [
        'City',
        'Condition',
        'Temperature (°C)',
        'Rain (%)',
        'Wind (km/h)',
        'Humidity (%)'
        ]

    # Extract rows of data
    rows = [
        [
            d['name'],
            d['condition'],
            d['temp'],
            d['daily_chance_of_rain'],
            d['maxwind_kph'],
            d['avghumidity']
        ] for d in data
    ]

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6.75))
    ax.axis('off')

    # Add title to the left
    title = "Today's Weather Forecast"
    plt.text(
        0.01,
        1.05,
        title,
        ha='left',
        va='center',
        fontsize=18,
        weight='bold',
        transform=ax.transAxes)

    # Add metadata to the rignt
    metadata = [
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "Source: weatherapi.com",
        "Engineer: victhengineer"
    ]
    for i, line in enumerate(metadata):
        plt.text(
            0.99,
            1.05 - (i * 0.05),
            line,
            ha='right',
            va='center',
            fontsize=12,
            style='italic',
            transform=ax.transAxes
            )

    # Add table
    table = Table(ax, bbox=[0, 0, 1, 0.85])

    # Add header row
    for i, header in enumerate(columns):
        cell = table.add_cell(
            0,
            i,
            width=1,
            height=0.25,
            text=header,
            loc='center',
            facecolor='lightgray')
        cell.set_text_props(fontweight='bold', fontsize=16)

    # Add data rows
    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_data in enumerate(row_data):
            cell = table.add_cell(
                row_idx + 1,
                col_idx,
                width=1,
                height=0.5,
                text=str(cell_data),
                loc="center")
            cell.set_text_props(fontweight="bold", fontsize=16)

    # Style adjustments
    for i in range(len(rows) + 1):  # Add cell borders
        for j in range(len(columns)):
            table[(i, j)].set_edgecolor('black')

    # Add table to axes
    ax.add_table(table)

    # Add diagonal watermark
    watermark_text = '@atmosbrief'
    plt.text(
        0.5, 0.5, watermark_text, fontsize=50, color="gray", alpha=0.2,
        ha="center", va="center", rotation=45, transform=fig.transFigure
    )
    # Create a direcory if doesnt
    save_dir = 'weather_updates'
    os.makedirs(save_dir, exist_ok=True)

    # Generate a formatted timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Define full file path
    file_path = os.path.join(save_dir, f"weather_table_{timestamp}.jpg")

    # Save the figure with a unique filename
    plt.savefig(
        file_path,
        format="jpg",
        dpi=600,
        bbox_inches="tight",
        pad_inches=0.4
    )
    print(f'Image Saved: {file_path}')
    return file_path
