"""
Simple tests
"""


from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(3, 5)
        self.assertEqual(res, 8)

    def test_subtract_numbers(self):
        res = calc.subtract(4, 8)
        self.assertEqual(res, -4)
