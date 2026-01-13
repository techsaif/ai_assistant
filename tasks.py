import os
import requests
import psutil
import wikipedia
from config import *

def open_app(app):
    if app == "chrome":
        os.system("start chrome")
    elif app == "calculator":
        os.system("calc")

def system_status():
    battery = psutil.sensors_battery()
    return f"Battery is {battery.percent}%"

def weather(city):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    res = requests.get(BASE_WEATHER_URL, params=params).json()
    return f"{res['weather'][0]['description']} with {res['main']['temp']}°C"

def wiki_search(query):
    return wikipedia.summary(query, sentences=2)
