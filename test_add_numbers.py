import unittest

from add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_integers(self) -> None:
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_floats(self) -> None:
        self.assertAlmostEqual(add_numbers(2.5, 1.5), 4.0)

    def test_add_negative_numbers(self) -> None:
        self.assertEqual(add_numbers(-4, 1), -3)


if __name__ == "__main__":
    unittest.main()
