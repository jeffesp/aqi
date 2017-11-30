from datetime import datetime
import json
import sqlite3

from weather import get_weather, COLS
from data import ensure_db_exists, add_weather 


db = sqlite3.connect('aqi.sqlite')
ensure_db_exists(db)

w = get_weather(*COLS)

add_weather(db, COLS[0], COLS[1], datetime.today(), json.dumps(w[0]._data))

db.commit()
