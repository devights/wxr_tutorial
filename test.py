import unittest
from weather import get_alerts, get_current_temperature, \
    get_current_windspeed, get_hourly_temperature
import datetime


class TestWeather(unittest.TestCase):
    def test_alert(self):
        alerts = get_alerts()
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]['event'], "Small Craft Advisory")
        self.assertEqual(alerts[0]['start'],
                         datetime.datetime(2020, 12, 13, 6, 0))
        self.assertEqual(alerts[0]['end'],
                         datetime.datetime(2020, 12, 13, 15, 0))

    def test_current_temp(self):
        temp = get_current_temperature()
        self.assertEqual(temp, 278.52)

    def test_wind(self):
        wind = get_current_windspeed()
        self.assertEqual(wind, 1.5)

    def test_hourly_temp(self):
        temps = get_hourly_temperature()
        self.assertEqual(len(temps), 48)
        self.assertEqual(temps[0]['time'],
                         datetime.datetime(2020, 12, 12, 22, 0))
        self.assertEqual(temps[0]['temp'], 278.52)
