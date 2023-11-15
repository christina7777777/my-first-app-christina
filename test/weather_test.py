# this is the "test/weather_test.py" file...

from app.weather import forecast_demo


def test_weather_app():

    assert forecast_demo("06070") == 202
