import sqlite3

CREATE_WEATHER = '''CREATE TABLE IF NOT EXISTS weather (
            lat REAL NOT NULL, 
            long REAL NOT NULL, 
            ts timestamp NOT NULL,
            value TEXT);'''
CREATE_WEATHER_INDEX = '\
    CREATE INDEX IF NOT EXISTS query_values ON weather (lat, long, ts DESC);'
INSERT_WEATHER = 'INSERT INTO weather VALUES (?, ?, ?, ?);'
SELECT_WEATHER = '\
    SELECT value FROM weather WHERE lat = ? AND long = ? AND ts = ?;'
SELECT_LATEST_WEATHER = '\
    SELECT value FROM weather WHERE lat = ? AND long = ? ORDER BY ts DESC LIMIT 1;'

def ensure_db_exists(data):
    data.execute(CREATE_WEATHER)
    data.execute(CREATE_WEATHER_INDEX)

def add_weather(data, *args):
    with data:
        data.execute(INSERT_WEATHER, args)

def find_weather(data, lat, lng, ts):
    return data.execute(SELECT_WEATHER, (lat, lng, ts))

def get_latest_weather(data, lat, lng):
    return data.execute(SELECT_LATEST_WEATHER, (lat, lng))

if __name__ == '__main__':
    db = sqlite3.connect('aqi.sqlite')
    ensure_db_exists(db)
    get_latest_weather(db, 39.954352, 116.466258)
