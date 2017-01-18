"""Test cases for the Fibonacci client using the unittest framework."""

import unittest
from fibcli import execute_fibonacci_query


class TestFibonacciCli(unittest.TestCase):
    """Test class for the Fibonacci client."""

    def test_execute_fib_query_succeeds_simple(self):
        """Execute a simple call using a known value and ensure the client
        properly executes and returns the expected value.
        """

        self.assertEqual(execute_fibonacci_query(7), str(13))

if __name__ == '__main__':
    """Main method to setup logging and initiate the test runner."""

    log_file_name = 'fibcli-test.log'
    log_file = open(log_file_name, "w")
    runner = unittest.TextTestRunner(log_file)

    unittest.main(testRunner=runner)

    log_file.close()
