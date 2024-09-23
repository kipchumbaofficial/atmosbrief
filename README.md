# atmosbrief

![atmosbrief](https://img.shields.io/twitter/follow/atmosbrief?style=social)

## Overview
**atmosbrief** is an automated Twitter bot that provides real-time weather updates for major cities around the world, focusing especially on cities in Africa. It uses the Weather API and the X (formerly Twitter) API to tweet weather conditions such as temperature, humidity, sunrise, sunset times, and more. It runs at scheduled times throughout the day to keep followers informed about the current and forecasted weather.

## Features
- Posts **daily forecasts** for selected cities at sunrise (Nairobi time).
- Shares **current weather updates** for African cities three times a day (7:00 AM, 12:00 PM, and 7:00 PM Nairobi time).
- Tweets include detailed weather information such as temperature, humidity, wind speed, and chance of rain.
- Uses relevant weather icons and emojis to visually enhance the updates.
- Automatically manages tweet formatting to ensure it fits within Twitter's character limits.

## How It Works
- **Weather API**: Fetches forecasted and current weather information for a set of predefined cities using [WeatherAPI](https://www.weatherapi.com/).
- **Twitter API (X API)**: Posts the weather updates on the [@atmosbrief](https://twitter.com/atmosbrief) Twitter account using the X API.
- **GitHub Actions**: Automates the bot’s scheduling for posting weather updates at specific times.
- **Time Zone**: The bot operates using the **Africa/Nairobi** time zone for scheduling posts.

## Cities Covered
The bot posts weather updates for the following cities:

### African Cities:
- Nairobi
- Cairo
- Johannesburg
- Kinshasa
- Addis Ababa
- Casablanca
- Lagos
- Abidjan
- Dodoma
- Accra

### Other Major Cities:
- London
- New York
- Sydney
- Tokyo
- Paris
- Buenos Aires
- Dubai

## Technology Stack
- **Python**: Main programming language used for the bot.
- **Tweepy**: Python library for accessing the X API.
- **WeatherAPI**: For retrieving weather data.
- **GitHub Actions**: For automating scheduled tasks.
- **pytz**: For handling time zone conversions.
- **Schedule**: Python package to schedule periodic tasks.

## Installation and Setup

### Prerequisites
- Python 3.x installed
- Twitter Developer Account for API access
- WeatherAPI Account for weather data access

### Environment Variables
You will need to set up the following environment variables for the bot to function properly. You can either store them in a `.env` file or configure them as GitHub Secrets if running the bot via GitHub Actions.

```bash
CONSUMER_KEY='your_X_API_key'
CONSUMER_SECRET='your_X_API_key_secret'
ACCESS_TOKEN='your_X_API_access_token'
ACCESS_TOKEN_SECRET='your_X_API_access_token_secret'
WEATHER_API_KEY='your_weather_API_key'
```

### Installing Dependencies
To install the bot's dependencies, run:
```bash
pip install -r requirements.txt
```
### Running the Bot Manually

You can also run the bot manually to post weather updates using the following commands:

For posting the daily forecast:
```bash
python3 bot/forecast.py
```
For posting the current weather for African cities:
```bash
python3 bot/post_current.py
```
### Contribution Guidelines
We welcome contributions from the community! To contribute to atmosbrief, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m "Added a new feature").
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request (PR) and describe the changes.

## Before contributing, please ensure you:

a) Adhere to the Python PEP8 style guide.
b) Run tests locally before submitting your pull request.

### Contact
For any inquiries or support, feel free to reach out:

X: [@atmosbrief](https://twitter.com/atmosbrief) | [@DevKipchumba](https://twitter.com/DevKipchumba)
Email: kipchumba.softwaredev@gmail.com