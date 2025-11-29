#!/usr/bin/env python3

from weather_app import get_location, get_weather
from config import API_KEY  # Keep your real key in config.py, ignored in git

def main():
    print("Fetching your location...!!!")
    location = get_location()
    print(f"📍 Location: {location['city']}, {location['region']}, {location['country']}")
    print("Fetching weather details...\n")

    weather = get_weather(location["lat"], location["lon"], API_KEY)

    if "main" not in weather:
        print("\n❌ Unable to fetch weather details.")
        print("➡ Error message:", weather.get("message", "Unknown error"))
        return

    print("\n🌦 Weather Details:")
    print(f"Temperature: {weather['main']['temp']}°C")
    print(f"Feels Like: {weather['main']['feels_like']}°C")
    print(f"Condition: {weather['weather'][0]['description'].title()}")
    print(f"Humidity: {weather['main']['humidity']}%")
    print(f"Wind Speed: {weather['wind']['speed']} m/s")
    print(f"Pressure: {weather['main']['pressure']} hPa")

if __name__ == "__main__":
    main()
# Testing CI pipeline auto-run - Testing