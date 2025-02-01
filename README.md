# atmosbrief

![atmosbrief](https://img.shields.io/twitter/follow/atmosbrief?style=social)

## Overview
**atmosbrief** is an automated bot that provides real-time weather updates for major
cities around the world. Originally focused on African cities, the bot now
supports updates for multiple continents. It fetches weather data from
[WeatherAPI](https://www.weatherapi.com/) and uses the X (formerly Twitter) API
to tweet detailed weather conditions—such as temperature, humidity, wind speed,
and chance of rain—in a visually enhanced table format. The bot is scheduled
to run at specific times of the day via GitHub Actions.

## Features
- Posts **daily forecasts** for selected cities at sunrise (Nairobi time).
- Shares **current weather updates** multiple times per day for cities across
  five major regions.
- Groups cities by continents using an internal dictionary with an Earth emoji
  for each region.
- Tweets include detailed weather data, visualized in a table with icons and
  emojis.
- Automatically manages tweet formatting to fit within X’s character limits.
- Uses GitHub Actions to schedule posts and manage automation.

## How It Works
- **Weather API**: Retrieves forecasted and current weather data for a set of
  predefined cities using WeatherAPI.
- **X API (Twitter API)**: Posts weather updates from the [@atmosbrief](https://twitter.com/atmosbrief)
  account with attached images of weather tables.
- **Dictionary Iteration**: The bot uses a dictionary where keys are continents
  (with an Earth emoji) and values are lists of five major cities (each from a
  different country). It iterates through this dictionary to fetch data, plot
  tables, and tweet updates.
- **GitHub Actions**: Automates scheduling and deployment. The bot runs at
  designated times (e.g., 7:30 AM EAT) based on a cron job.
- **Time Zone**: Operates on the **Africa/Nairobi** time zone for scheduling.

## Cities Covered
The bot posts weather updates for major cities grouped by five regions:

### Regions and Cities:
- **🌏 Asia**: Tokyo, Delhi, Shanghai, Karachi, Dhaka
- **🌍 Africa**: Lagos, Cairo, Kinshasa, Johannesburg, Nairobi
- **🌍 Europe**: Moscow, London, Berlin, Madrid, Rome
- **🌎 North America**: Mexico City, New York City, Toronto, Havana, Guatemala City
- **🌎 South America & Oceania**: São Paulo, Buenos Aires, Lima, Santiago, Sydney

## Technology Stack
- **Python**: Core language for bot logic.
- **Tweepy**: For accessing and interacting with the X API.
- **WeatherAPI**: Provides real-time and forecasted weather data.
- **GitHub Actions**: Automates scheduled execution and deployment.
- **Matplotlib**: Generates weather data tables as images.

### Contribution Guidelines
We welcome contributions from the community! To contribute to atmosbrief, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m "Added a new feature").
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request (PR) and describe the changes.

#### Before contributing, please ensure you:

- Adhere to the Python PEP8 style guide.
- Run tests locally before submitting your pull request.

### Contact
For any inquiries or support, feel free to reach out:

X: [@victhengineer](https://twitter.com/atmosbrief) | [@victhengineer](https://twitter.com/victhengineer)
Email: kipchumba.softwaredev@gmail.com

> **Note**: The bot is limited to 17 tweets per day due to Twitter's 50 request limit within a 24-hour period. As a result, only a selected number of cities are included in the weather updates.
