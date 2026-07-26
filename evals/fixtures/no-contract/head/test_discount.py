import unittest

from discount import apply_discount, format_price


class TestApplyDiscount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(apply_discount(100.0, 0.2), 80.0)

    def test_zero(self):
        self.assertEqual(apply_discount(50.0, 0.0), 50.0)


class TestFormatPrice(unittest.TestCase):
    def test_grouping(self):
        self.assertEqual(format_price(1234.5), "$1,234.50")

    def test_small(self):
        self.assertEqual(format_price(0.5), "$0.50")


if __name__ == "__main__":
    unittest.main()
