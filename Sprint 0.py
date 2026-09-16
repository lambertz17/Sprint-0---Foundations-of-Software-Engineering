import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)


if __name__ == "__main__":
    unittest.main()

    