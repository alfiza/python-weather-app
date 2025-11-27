import requests

API_KEY = "9e4d8fbe0c3993f39efca8af1cdc9505"   # replace with your real key

def get_location():
    url = "https://ipinfo.io/json"
    response = requests.get(url).json()
    loc = response["loc"].split(",")
    return {
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country"),
        "lat": loc[0],
        "lon": loc[1]
    }

def get_weather(lat, lon, api_key):
    """Get weather data from OpenWeatherMap"""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return response


