from os import environ
from datetime import date, datetime, timedelta
from darksky import forecast

COLS = 40.0859627, -83.0111861
BEIJING = 39.954352, 116.466258


def get_weather(lat, lng, start_date=None, num_days=1):
    def make_request(dte):
        with forecast(key, lat, lng, time=int(dte.timestamp())) as fcst:
            return fcst.daily[0]

    key = environ.get('DARK_SKY_KEY')
    if start_date is None:
        start_date = datetime.today()
    dates = [start_date + timedelta(days=d) for d in range(0, num_days)]

    return [make_request(d) for d in dates]


def print_weather(day):
    data = dict(day=date.strftime(date.fromtimestamp(day.time), '%a'),
                sum=day.summary,
                tMin=day.temperatureMin,
                tMax=day.temperatureMax)
    print('{day}: {sum} Temp range: {tMin} - {tMax}'.format(**data))


if __name__ == '__main__':
    _ = [print_weather(d) for d in get_weather(*COLS, num_days=10)]
    