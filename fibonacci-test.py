"""Unit tests for the Fibonacci class."""

import unittest
from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    """Test class for the Fibonacci client."""

    def test_calculate(self):
        """Execute the calculate method using a known value and ensure the
        client properly executes and returns the expected value.
        """

        fibonacci = Fibonacci(7)
        self.assertEqual(fibonacci.calculate(), 13)


if __name__ == '__main__':
    """Main method to setup logging and initiate the test runner."""

    log_file_name = 'fibonacci-test.log'
    log_file = open(log_file_name, "w")
    runner = unittest.TextTestRunner(log_file)

    unittest.main(testRunner=runner)

    log_file.close()
