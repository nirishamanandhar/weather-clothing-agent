import os
import requests
from .models import WeatherRequest, WeatherData


def get_weather(request: WeatherRequest) -> WeatherData:
    """Get the weather for a given location and time."""
    api_key = os.getenv("WEATHER_API_KEY")
    url = ( 
        "https://api.openweathermap.org/data/2.5/weather" 
        f"?q={request.location}&appid={api_key}&units=metric" 
        )
    raw = requests.get(url).json() 
    return WeatherData( 
        temperature_c=raw["main"]["temp"], 
        feels_like_c=raw["main"]["feels_like"], 
        wind_speed_kph=raw["wind"]["speed"] * 3.6, 
        humidity=raw["main"]["humidity"], 
        condition=raw["weather"][0]["description"], 
        rain_probability=raw.get("rain", {}).get("1h", 0.0) 
    )