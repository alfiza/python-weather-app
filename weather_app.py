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

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    return response

def main():
    print("Fetching your location...")
    location = get_location()

    print(f"📍 Location: {location['city']}, {location['region']}, {location['country']}")
    print("Fetching weather details...\n")

    weather = get_weather(location["lat"], location["lon"])

    # 👉 PRINT FULL RESPONSE TO SEE ERRORS
    print("API Response:", weather)

    # 👉 CHECK IF ERROR EXISTS
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
