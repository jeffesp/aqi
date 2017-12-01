from os import environ
from datetime import date, datetime, timedelta
import requests
import backoff

BASE_URL = 'https://api.darksky.net/forecast/{}/{},{},{}?exclude=currently,minutely,flags'

def get_weather(lat, lng, start_date=None, num_days=1):

    def fatal_code(e):
        return 400 <= e.response.status_code < 500

    @backoff.on_exception(
        backoff.expo,
        (requests.exceptions.Timeout, requests.exceptions.ConnectionError),
        max_tries=5,
        giveup=fatal_code)
    def make_request(key, dte):
        accept_gzip = {'accept-encoding': 'gzip'}
        since_epoch = int(dte.timestamp())
        response = requests.get(BASE_URL.format(key, lat, lng, since_epoch), headers=accept_gzip)
        response.raise_for_status()
        return response.json()

    if num_days < 1:
        raise Exception('Cannot get forecast for fewer than one day.')

    key = environ.get('DARK_SKY_KEY')
    if start_date is None:
        start_date = datetime.today()

    if num_days == 1:
        return make_request(key, start_date)
    else:
        return [make_request(key, start_date + timedelta(days=d)) for d in range(0, num_days)]


def print_weather(response):
    day = response['daily']['data'][0]
    data = dict(day=date.strftime(date.fromtimestamp(day['time']), '%a'),
                sum=day['summary'],
                tMin=day['temperatureMin'],
                tMax=day['temperatureMax'])
    print('{day}: {sum} Temp range: {tMin} - {tMax}'.format(**data))


if __name__ == '__main__':
    _ = [print_weather(d) for d in get_weather(40.0859627, -83.0111861, num_days=3)]
    