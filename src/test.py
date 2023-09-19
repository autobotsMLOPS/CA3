import unittest
from main import add, sub, mul, div, modu, square_root, power, factorial


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(1, 2), -1)

    def test_mul(self):
        self.assertEqual(mul(1, 2), 2)

    def test_div(self):
        self.assertEqual(div(1, 2), 0.5)
        with self.assertRaises(ValueError):
            div(1, 0)
    def test_modu(self):
        self.assertEqual(modu(10, 5), 0)
        with self.assertRaises(ValueError):
            modu(1, 0)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()