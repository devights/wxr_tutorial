import requests

API_KEY = ""
URL_BASE = "https://api.openweathermap.org/data/2.5/"


"""
Makes a request to the OpenWeather Onecall API.
https://api.openweathermap.org/data/2.5/onecall?
lat={lat}&lon={lon}&exclude={part}&appid={API key}

"""


def get_onecall():
    lat = 47.606
    lon = -122.332

    url = f"{URL_BASE}onecall?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)
    return response.content
