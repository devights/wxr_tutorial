from mock_client import get_onecall
import json
import datetime


def get_data():
    # Data is in JSON format, this turns it from text into a python dictionary
    # Makes it easy to access data by key name, loop over, etc
    # Data documentation: https://openweathermap.org/api/one-call-api
    raw_data = get_onecall()

    # json.loads load from the string raw_data
    return json.loads(raw_data)


def get_alerts():
    data = get_data()
    alert_data = []
    # This is in a try so that if there are no alerts (it would throw the
    # KeyError if the 'alerts' key didn't exist) we return an empty list
    # instead of crashing on the missing key.  The "Python" way is to try
    # and fail rather than test if the key existed first
    try:
        alerts = data['alerts']
        for alert in alerts:
            alert_start = get_datettime_from_timestamp(alert['start'])
            alert_end = get_datettime_from_timestamp(alert['end'])
            alert_event = alert['event']
            parsed_alert = {'start': alert_start,
                            'end': alert_end,
                            'event': alert_event}
            alert_data.append(parsed_alert)
    except KeyError as ex:
        pass
    return alert_data


def get_datettime_from_timestamp(timestamp):
    # The api uses unix time (# of seconds since 1970) to store timestamps,
    # eg 1607839200, this turns them into useful datetime objects.  We can
    # do timezone conversion from UTC on these
    return datetime.datetime.utcfromtimestamp(timestamp)


def get_current_temperature():
    # Should return the current temperature
    return NotImplemented


def get_current_windspeed():
    # Should return the current windspeed
    return NotImplemented


def get_hourly_temperature():
    # should return a list of dictionaries with a time and temperature
    # eg [{'time': time, 'temp': temp}, {'time': time, 'temp': temp}]
    return NotImplemented
