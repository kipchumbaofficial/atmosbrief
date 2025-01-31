#!/usr/bin/env python3
'''Test the functions
'''
from atmosbrief import fetch_weather, plot_weather_table

cities = ["Nairobi", "Mombasa", "Kisumu", "Marsabit", "Eldoret"]
weather_info = fetch_weather(cities)
plot_weather_table(weather_info)
