"""Unit tests for the Fibonacci class."""

import unittest
from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    """Test class for the Fibonacci client."""

    def test_calculate_valid_sequence_value_succeeds(self):
        """Execute the calculate method using a known value and ensure the
        expected value is returned.
        """

        fibonacci = Fibonacci(7)
        self.assertEqual(fibonacci.calculate(), 13)

    def test_calculate_zero_sequence_value_succeeds(self):
        """Execute the calculate method using a zero value and ensure the
        return value is 0.
        """

        fibonacci = Fibonacci(0)
        self.assertEqual(fibonacci.calculate(), 0)

    def test_calculate_negative_sequence_value_fails(self):
        """Execute the calculate method using a negative value and ensure the
        TypeError exception is raised.
        """

        fibonacci = Fibonacci(-1)
        self.assertRaises(TypeError, fibonacci.calculate)

    def test_calculate_string_sequence_value_fails(self):
        """Execute the calculate method using a string value and ensure the
        TypeError exception is raised.
        """

        fibonacci = Fibonacci("string")
        self.assertRaises(TypeError, fibonacci.calculate)


if __name__ == '__main__':
    """Main method to setup logging and initiate the test runner."""

    log_file_name = 'fibonacci-test.log'
    log_file = open(log_file_name, "w")
    runner = unittest.TextTestRunner(log_file)

    unittest.main(testRunner=runner)

    log_file.close()
