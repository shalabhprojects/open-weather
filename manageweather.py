import requests

BASE_URL = 'http://api.openweathermap.org'
PATH = '/data/2.5/weather?'
API_KEY = 'appid=e6974292627b33bcb8ee3c985d52c2d5'

def get_weather(query):
    return requests.get(BASE_URL + PATH + API_KEY + query)