import unittest
from ex_11_1_city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Test case for city_functions."""

    def test_city_country(self):
        """Testing format for Maracaibo, Venezuela."""
        locations = city_country("maracaibo", "venezuela")
        self.assertEqual(locations, "Maracaibo, Venezuela")

if __name__ == "__main__":
    unittest.main()