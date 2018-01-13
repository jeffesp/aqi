from datetime import datetime

def get_latest():
    return {'date':123123123123, 'aqi': 34, 'pm25': 8.2}

def parse_entry(rss_item):
    reading_time = int(datetime.strptime(rss_item.readingdatetime, '%m/%d/%Y %H:%M:%S %p').timestamp())
    return {'date': reading_time,  'aqi': int(rss_item.aqi), 'pm25': float(rss_item.conc)}
