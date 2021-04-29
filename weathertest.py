import unittest
from manageweather import get_weather

class TestGetWeather(unittest.TestCase):

    def test_get_weather_by_city(self):
        response = get_weather('&q=London')
        self.assertEqual(response.status_code, 200, "Get Weather Response Status")
        self.assertEqual(response.json()['name'], 'London', "City Name")

    def test_get_weather_by_lat_lon(self):
        response = get_weather('&lat=-0.1257&lon=51.5085')
        self.assertEqual(response.status_code, 200, "Get Weather Response Status")
        self.assertEqual(response.json()['coord']['lat'], -0.1257, "Latitude")
        self.assertEqual(response.json()['coord']['lon'], 51.5085, "Longitude")

    def test_get_weather_by_zipcode(self):
        response = get_weather('&zip=06902')
        self.assertEqual(response.status_code, 200, "Get Weather Response Status")
        self.assertEqual(response.json()['name'], 'Stamford', "City Name")

if __name__ == '__main__':
    unittest.main()