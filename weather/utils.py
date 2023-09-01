from datetime import datetime
from os import environ as env
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

DATETIME_FORMAT = '%H:%M:%S'


def convert_utc_timestamp_time(input_time):
    if isinstance(input_time, datetime):
        decode_time = input_time
    else:
        decode_time = datetime.utcfromtimestamp(input_time)
    time_format = decode_time.strftime(DATETIME_FORMAT)
    return time_format


def get_weather(city_name, measure_type):

    response = requests.get(
        env.get('WEATHER_URL').format(city_name, measure_type, env.get('APP_KEY'))
    ).json()
    return {
        'message': f'Hi, this is a daly report for actual weather on this time '
                   f'{convert_utc_timestamp_time(datetime.now())}',
        'weather': {
            'City': city_name,
            'Country': response['sys']['country'],
            'General': response['weather'][0]['description'],
            'Temperature': response['main']['temp'],
            'Feels Like': response['main']['feels_like'],
            'Humidity': response['main']['humidity'],
            'Sunrise Time': convert_utc_timestamp_time(response['sys']['sunrise']),
            'Sunset Time': convert_utc_timestamp_time(response['sys']['sunset']),
            'Icon': response['weather'][0]['icon']
        }
    }


pprint(get_weather('Dreux', 'Metric'))
