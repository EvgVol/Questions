
class BaseWeatherException(Exception):
    ...

class CityNotFoundError(BaseWeatherException):

    def __init__(self, city, message) -> None:
        super().__init__(message)
        self.city = city



WEATHER_FORECAST = {
    "moscow": {"temp": 20, "humidity": 40, "rain_chance": 70,},
    "sochi": {"temp": 30, "humidity": 50, "rain_chance": 20,},
}


def get_weather(city: str) -> dict:
    if weather := WEATHER_FORECAST.get(city.lower()):
        return weather

    message = f"no weather for {city}"
    raise CityNotFoundError(city, message)


def rain_tomorrow(city: str) -> bool | None:
    try:
        weather = get_weather(city)
    except CityNotFoundError:
        print( )
        return

    return weather["rain_chance"] >= 50


if __name__ == "__main__":
    print("rain in Moscow", rain_tomorrow("Moscow"))
    print("rain in Voronezh", rain_tomorrow("Voronezh"))
    print("rain in Sochi", rain_tomorrow("Sochi"))
