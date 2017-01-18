"""Test cases for the Fibonacci client using the unittest framework."""

import unittest
from fibcli import execute_fibonacci_query


class TestFibonacciCli(unittest.TestCase):
    """Test class for the Fibonacci client."""

    def test_execute_fib_query_valid_sequence_value_succeeds(self):
        """Execute the execute_fib_query method using a known value and ensure
        the client properly executes and returns the expected value.
        """

        self.assertEqual(execute_fibonacci_query(7), str(13))

    def test_execute_fib_query_zero_sequence_value_succeeds(self):
        """Execute the execute_fib_query method using a zero value and ensure
        the client succeeds, returning the value 0.
        """

        self.assertEqual(execute_fibonacci_query(0), str(0))

    def test_execute_fib_query_negative_sequence_value_fails(self):
        """Execute the execute_fib_query method using a negative value and
        ensure the raises a general exception.
        """

        self.assertRaises(Exception, execute_fibonacci_query, -1)

    def test_execute_fib_query_string_sequence_value_fails(self):
        """Execute the execute_fib_query method using a string value and
        ensure the raises a general exception.
        """

        self.assertRaises(Exception, execute_fibonacci_query, "string")

if __name__ == '__main__':
    """Main method to setup logging and initiate the test runner."""

    log_file_name = 'fibcli-test.log'
    log_file = open(log_file_name, "w")
    runner = unittest.TextTestRunner(log_file)

    unittest.main(testRunner=runner)

    log_file.close()
