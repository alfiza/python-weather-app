from flask import Flask
from weather_app import get_location, get_weather
from config import API_KEY

app = Flask(__name__)

@app.route('/')
def home():
    location = get_location()
    weather = get_weather(location["lat"], location["lon"], API_KEY)
    if "main" not in weather:
        return f"Unable to fetch weather details. Error: {weather.get('message', 'Unknown error')}"
    
    return f"""
    <h2>!!!***Weather Details***---!!!</h2>
    <p>Location: {location['city']}, {location['region']}, {location['country']}</p>
    <p>Temperature: {weather['main']['temp']}°C</p>
    <p>Feels Like: {weather['main']['feels_like']}°C</p>
    <p>Condition: {weather['weather'][0]['description'].title()}</p>
    <p>Humidity: {weather['main']['humidity']}%</p>
    <p>Wind Speed: {weather['wind']['speed']} m/s</p>
    <p>Pressure: {weather['main']['pressure']} hPa</p>
    """
