# this is the "test/weather_test.py" file...

from app.weather import display_forecast


def test_weather_app():

    assert display_forecast("06070") == True
