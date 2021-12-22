#Exercise 11.1
#Test  city_functions.py
import unittest
from city_functions import get_formatted_name
class NamesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""
	def test_city_country(self):
		"""Do names like 'Tokyo Japan' work?"""
		formatted_name = get_formatted_name('tokyo', 'japan')
		self.assertEqual(formatted_name, 'Tokyo,Japan')
unittest.main()

