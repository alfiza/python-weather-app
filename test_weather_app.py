import pytest
from unittest.mock import patch
from weather_app import get_location, get_weather

# ---- Test get_location ----
@patch("weather_app.requests.get")
def test_get_location(mock_get):
    """
    Test get_location() by mocking the IP location API response
    """
    # Mocked API response
    mock_get.return_value.json.return_value = {
        "city": "Dublin",
        "region": "Leinster",
        "country": "IE",
        "loc": "53.333,-6.249"
    }

    loc = get_location()
    assert loc["city"] == "Dublin"
    assert loc["region"] == "Leinster"
    assert loc["country"] == "IE"
    assert loc["lat"] == "53.333"
    assert loc["lon"] == "-6.249"

# ---- Test get_weather ----
@patch("weather_app.requests.get")
def test_get_weather(mock_get):
    """
    Test get_weather() by mocking OpenWeatherMap API response
    """
    # Mocked API response
    mock_get.return_value.json.return_value = {
        "main": {
            "temp": 12,
            "feels_like": 11,
            "humidity": 80,
            "pressure": 1012
        },
        "weather": [{"description": "light rain"}],
        "wind": {"speed": 5}
    }

    weather = get_weather("53.333", "-6.249", "fake_api_key")
    assert weather["main"]["temp"] == 12
    assert weather["main"]["feels_like"] == 11
    assert weather["main"]["humidity"] == 80
    assert weather["main"]["pressure"] == 1012
    assert weather["weather"][0]["description"] == "light rain"
    assert weather["wind"]["speed"] == 5
