import unittest

import pytest


def add(x, y):
    return x + y


# class TestAddition():
#     def test_add_positive_numbers(self):
#         assert (add(3, 5), 8)
#
#     def test_add_negative_numbers(self):
#         assert (add(-1, -2), -3)
#
#     def test_add_zero(self):
#         assert (add(0, 0), 0)
#
#     def test_add_mixed(self):
#         assert (add(-1, 1), 0)


# @pytest.mark.parametrize("a,b, expected", [
(3, 5, 8)


# ])


@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]


# def test_sum(sample_list):
#     assert sum(sample_list) == 15
#
#
# def test_len(sample_list):
#     assert len(sample_list) == 5


# def calc(operation, a, b):
#     if operation == "add":
#         return a + b
#     elif operation == "sub":
#         return a - b
#     elif operation == "mul":
#         return a * b
#
#     elif operation == "div":
#         if b == 0:
#             raise ZeroDivisionError("Zero Division")
#         return a / b
#     else:
#         raise ValueError(f"Unknown {operation} operation")
#
#
# @pytest.mark.parametrize("operation , a,b,expected ", [
#     ("add", 3, 5, 8),
#     ("sub", 10, 4, 6),
#     ("mul", 2, 3, 6),
#     ("div", 8, 2, 4)
# ])
# def test_cal(operation, a, b, expected):
#     assert calc(operation, a, b) == expected, "Wrong"

#
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Zero Division")
#     return a / b
#
#
# def test_divide_success():
#     assert divide(10, 2) == 5
#
# def test_divide_error():
#     with pytest.raises(ZeroDivisionError):
#         divide(10,0)


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, x):
        self.value += x

    def subtract(self, x):
        self.value -= x

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        self.calc

    def test_add(self):
        self.assertEqual(self.calc.add(5),5)
        self.assertEqual(self.calc.add(3),5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5),5)



def to_upper(text):
    return text.upper()

def split_text(text, delimeter = " "):
    if not isinstance(delimeter, str):
        raise TypeError("Рядком раздельниеи передаем")
    return text.split(delimeter)

def test_to_upper():
    assert to_upper("python") =="PYTHON"

def test_split_text():
    text = "hello world"
    assert split_text(text) == ["hello", "world"]

def test_split_text():
    text = "hello world"
    assert split_text(text) == ["hello", "world"]