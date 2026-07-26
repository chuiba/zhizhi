import unittest

from checkout import total
from config import load_config
from discount import apply_discount


class TestApplyDiscount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(apply_discount(100.0, 0.2), 80.0)


class TestLoadConfig(unittest.TestCase):
    def test_default_tax(self):
        self.assertEqual(load_config()["tax_rate"], 0.08)

    def test_rejects_negative(self):
        with self.assertRaises(ValueError):
            load_config({"tax_rate": -0.1})


class TestTotal(unittest.TestCase):
    def test_tax_applied_by_default(self):
        self.assertEqual(total(100.0, 0.2), 86.4)

    def test_override_keeps_old_behavior(self):
        self.assertEqual(total(100.0, 0.2, {"tax_rate": 0.0}), 80.0)


if __name__ == "__main__":
    unittest.main()
