import unittest

from discount import apply_discount


class TestApplyDiscount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(apply_discount(100.0, 0.2), 80.0)

    def test_zero(self):
        self.assertEqual(apply_discount(50.0, 0.0), 50.0)


if __name__ == "__main__":
    unittest.main()
