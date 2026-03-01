from pydantic import BaseModel
from typing import Optional


class WeatherRequest(BaseModel):
    location: str = "Dublin" 
    time: Optional[str] = None


class WeatherData(BaseModel):
    temperature_c: float 
    feels_like_c: float 
    wind_speed_kph: float 
    humidity: float 
    condition: str 
    rain_probability: float
