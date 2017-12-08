from datetime import datetime, timedelta
import sqlite3

from weather import get_weather
from data import ensure_db_exists, get_latest_weather, add_weather, get_timestamp

COLS = 40.0859627, -83.0111861
BEIJING = 39.954352, 116.466258

def import_data():
    db = sqlite3.connect('aqi.sqlite')
    ensure_db_exists(db)

    last_weather = get_latest_weather(db, *BEIJING)
    latest = get_timestamp(last_weather['daily']['data'][0]['time'], last_weather['timezone'])

    forecast = get_weather(*BEIJING, start_date=latest+timedelta(days=1), num_days=(datetime.today - latest).days)
    for day in forecast:
        add_weather(db, BEIJING, day)

    db.commit()


def import_airquality():
    pass