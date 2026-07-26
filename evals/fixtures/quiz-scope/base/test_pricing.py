import unittest

from checkout import total
from discount import apply_discount


class TestApplyDiscount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(apply_discount(100.0, 0.2), 80.0)


class TestTotal(unittest.TestCase):
    def test_no_tax_by_default(self):
        self.assertEqual(total(100.0, 0.2), 80.0)


if __name__ == "__main__":
    unittest.main()
