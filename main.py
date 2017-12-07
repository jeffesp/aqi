from datetime import datetime
import json
import sqlite3

from weather import get_weather, print_weather
from data import ensure_db_exists, add_weather

COLS = 40.0859627, -83.0111861
BEIJING = 39.954352, 116.466258

db = sqlite3.connect('aqi.sqlite')
ensure_db_exists(db)

w = get_weather(*BEIJING)

print_weather(w)
add_weather(db, BEIJING, datetime.today(), w)

db.commit()
