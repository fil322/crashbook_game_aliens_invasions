import unittest
from city_function import get_city_country

class CitiesTestCase(unittest.TestCase):
    """Тесты для 'city_function.py'."""

    def test_city_country(self):
        """Данные такие как 'santiago’ и ‘chile’, дают правильную строку"""
        formatted_city_country = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Данные такие как 'santiago’, ‘chile’ , 'population' , дают правильную строку"""
        formatted_city_country = get_city_country('santiago', 'chile', 50000)
        self.assertEqual(formatted_city_country, 'Santiago, Chile - population 50000')