import unittest
from ex_11_2_population import city_country

class CitiesTestCase(unittest.TestCase):
    """Test case for city_functions."""

    def test_city_country(self):
        """Testing format for Maracaibo, Venezuela."""
        location = city_country("maracaibo", "venezuela")
        self.assertEqual(location, "Maracaibo, Venezuela")

    def test_population(self):
        """Testing the function if population is available."""
        location = city_country("maracaibo", "venezuela", 4000000)
        self.assertEqual(location, "Maracaibo, Venezuela - Population 4000000")

if __name__ == "__main__":
    unittest.main()