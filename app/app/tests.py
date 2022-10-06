"""
Sample tests
"""

from django.test import SimpleTestCase
from rest_framework.test import APIClient

from app import calc

class CalcTests(SimpleTestCase):
    """
    Test the calc modules
    """

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted together"""
        res = calc.subtract(5, 6)
        self.assertEqual(res, -1)