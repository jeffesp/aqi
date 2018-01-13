from nose import with_setup
import feedparser

from .. import air_quality

class TestAirQualityParsing(object):


    def test_read_rss_item(self):
        parsed = feedparser.parse('../sample-airquality.xml')

        result = air_quality.parse_entry(parsed.entries[0])

        assert result['date'] == 1512644400
        assert result['aqi'] == 34
        assert result['pm25'] == 8.0



