import unittest 
from unittest import TestCase
from price_discount import discount  


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    # TODO more unit tests here. Each test should test one scenario
    def test_discount_with_more_than_three_items(self):
        result = discount([15, 8, 10, 5, 20])
        self.assertEqual(result, 5)

    def test_discount_with_empty_list(self):
        result = discount([])
        self.assertIsNone(result)

    def test_discount_with_same_item_prices(self):
        result = discount([7, 7, 7, 7])
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()