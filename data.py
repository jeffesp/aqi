import sqlite3
import json
from datetime import datetime
from pytz import timezone, utc

CREATE_WEATHER = '''CREATE TABLE IF NOT EXISTS weather (
            lat REAL NOT NULL, 
            long REAL NOT NULL, 
            ts timestamp NOT NULL,
            value TEXT);'''
CREATE_WEATHER_INDEX = '\
    CREATE UNIQUE INDEX IF NOT EXISTS query_values ON weather (lat, long, ts DESC);'
INSERT_WEATHER = 'INSERT INTO weather VALUES (?, ?, ?, ?);'
SELECT_WEATHER = '\
    SELECT value FROM weather WHERE lat = ? AND long = ? AND ts = ?;'
SELECT_LATEST_WEATHER = '\
    SELECT value FROM weather WHERE lat = ? AND long = ? ORDER BY ts DESC LIMIT 1;'

CREATE_AIR_QUALITY = '''CREATE TABLE IF NOT EXISTS air_quality (
    lat REAL NOT NULL,
    long REAL NOT NULL,
    ts timestamp NOT NULL,
    value TEXT);'''
CREATE_AIR_QUALITY_INDEX = '\
    CREATE UNIQUE INDEX IF NOT EXISTS query_values ON air_quality (lat, long, ts DESC);'
INSERT_AIR_QUALITY = 'INSERT INTO air_quality VALUES (?, ?, ?, ?);'
SELECT_AIR_QUALITY = '\
    SELECT value FROM air_quality WHERE lat = ? AND long = ? AND ts = ?;'
SELECT_LATEST_AIR_QUALITY = '\
    SELECT value FROM air_quality WHERE lat = ? AND long = ? ORDER BY ts DESC LIMIT 1;'

def ensure_db_exists(data):
    data.execute(CREATE_WEATHER)
    data.execute(CREATE_WEATHER_INDEX)
    data.execute(CREATE_AIR_QUALITY)
    data.execute(CREATE_AIR_QUALITY_INDEX)

def get_timestamp(epoch_seconds, tz_string):
    zone = timezone(tz_string)
    stamp = datetime.fromtimestamp(epoch_seconds, zone)
    return utc.normalize(stamp)

def add_weather(data, location, value):
    time_stamp = get_timestamp(data)
    with data:
        data.execute(INSERT_WEATHER,
                     (location[0], location[1], time_stamp, json.dumps(value)))

def find_weather(data, lat, lng, ts):
    return [json.loads(v[0]) for v in data.execute(SELECT_WEATHER, (lat, lng, ts)).fetchall()]

def get_latest_weather(data, lat, lng):
    cursor = data.cursor()
    value = cursor.execute(SELECT_LATEST_WEATHER, (lat, lng)).fetchone()
    if value:
        return json.loads(value[0])
    else:
        return None

def add_air_quality(data, location, value):
    time_stamp = get_timestamp(, data['timezone'])
    with data:
        data.execute(INSERT_AIR_QUALITY,
                     (location[0], location[1], time_stamp, json.dumps(value)))

def get_latest_air_quality(data, lat, lng):
    cursor = data.cursor()
    value = cursor.execute(SELECT_LATEST_AIR_QUALITY, (lat, lng)).fetchone()
    if value:
        return json.loads(value[0])
    else:
        return None

if __name__ == '__main__':
    db = sqlite3.connect('aqi.sqlite')
    ensure_db_exists(db)
    get_latest_weather(db, 39.954352, 116.466258)

