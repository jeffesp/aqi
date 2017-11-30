import sqlite3


def ensure_db_exists(data):
    data.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            lat REAL NOT NULL, 
            long REAL NOT NULL, 
            ts timestamp NOT NULL,
            value TEXT);''')
    data.execute(
        'CREATE INDEX IF NOT EXISTS query_values ON weather (lat, long, ts);')

def add_weather(data, *args):
    with data:
        data.execute('INSERT INTO weather VALUES (?, ?, ?, ?);', args)

def find_weather(data, lat, long, ts):
    return data.execute('SELECT value FROM weather WHERE lat = ? AND long = ? AND ts = ?',
               (lat, long, ts))

if __name__ == '__main__':
    db = sqlite3.connect('aqi.sqlite')
    ensure_db_exists(db)
