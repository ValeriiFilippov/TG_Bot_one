from config import WEATHER_APP_ID
import aiohttp
from typing import Tuple


async def get_weather(city: str) -> Tuple[str, str]:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_APP_ID}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            code: str = data["cod"]
            if code == "404":
                return 'City not found!', code

            city: str = data["name"]
            try:
                main = data["weather"][0]["main"]
            except IndexError:
                main = ''
            temp: int = int(data["main"]["temp"]) - 273
            wind: str = data["wind"]["speed"]
            humidity: str = data["main"]["humidity"]
            info = f'{city}\n{main}\nTemperature: {temp}\nWind: {wind}\nH: {humidity}%'
            return info, code
