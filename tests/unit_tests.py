import unittest


def add(x, y):
    return x + y


class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_mixed(self):
        self.assertEqual(add(-1, 1), 0)
