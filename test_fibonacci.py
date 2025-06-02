import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def test_generate_series_10(self):
        fib = Fibonacci(10)
        self.assertEqual(fib.generate_series(), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_generate_series_0(self):
        fib = Fibonacci(0)
        self.assertEqual(fib.generate_series(), [])

    def test_generate_series_1(self):
        fib = Fibonacci(1)
        self.assertEqual(fib.generate_series(), [0])

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            Fibonacci(-5)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(ValueError):
            Fibonacci(3.5)

if __name__ == "__main__":
    unittest.main()
