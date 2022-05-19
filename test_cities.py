import unittest
from city_functions import get_formatted_city_name

class CitiesTestCase(unittest.TestCase):
    """Tests for 'cities_functions.py'."""
    def test_city_country(self):
        """Does 'shanghai, china' work?"""
        formatted_city_name = get_formatted_city_name('shanghai', 'china')
        self.assertEqual(formatted_city_name, 'Shanghai, China')

    def test_city_country_population(self):
        """Does 'shanghai, china, 5000' work?"""
        formatted_city_name = get_formatted_city_name('shanghai', 'china', '5000000')
        self.assertEqual(formatted_city_name, 'Shanghai, China - population 5000000')

if __name__ == '__main__':
    unittest.main()
