import unittest

from application.main import (convert_month_to_days, convert_week_to_days)


class TestUtitlityFunctions(unittest.TestCase):

    def test_convert_months_to_days(self):
        two_months = convert_month_to_days(2)
        five_months = convert_month_to_days(5)

        self.assertIsInstance(convert_month_to_days(2), int)
        self.assertEqual(two_months, 30 * 2)
        self.assertEqual(five_months, 30*5)

    def test_convert_week_to_days(self):
        two_weeks = convert_week_to_days(2)
        five_weeks = convert_week_to_days(5)

        self.assertIsInstance(convert_week_to_days(2), int)
        self.assertEqual(two_weeks, 7 * 2)
        self.assertEqual(five_weeks, 7*5)
