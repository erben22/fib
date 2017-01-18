"""Test cases for the Fibonacci client using the unittest framework."""

import unittest
import threading
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

    def test_execute_fib_query_decent_sequence_request_succeeds(self):
        """Execute the execute_fib_query method using desired sequence that is
        of a decent size, and ensure the expected value is returned.
        """

        expected_value = (
            "34774673918037020105251744060433596978868493492784371065735223930"
            "41216496868459679756364593924530533774930268750207447601458424017"
            "92378749321113719919618588095724485583919541019961884523908359133"
            "457357334538791778480910430756107407761555218113998374287548487")

        self.assertEqual(execute_fibonacci_query(1234), expected_value)

    def test_execute_fib_query_large_sequence_request_succeeds(self):
        """Execute the execute_fib_query method using desired sequence that is
        very large and ensure a non-zero value is returned.  Expected runtime
        on a somewhat modern computer is in the neighborhood of 30s.
        """

        fibonacci_value = execute_fibonacci_query(1234567)
        self.assertTrue(fibonacci_value)

    def execute_concurrent_request(self, desired_sequence):
        """Helper method to execute a client request in a thread context.
            Just ensuring here we get a valid valud returned, but not actually
            worried about the exact value.
        """

        self.assertTrue(execute_fibonacci_query(desired_sequence))

    def test_execute_fib_query_concurrent_requests_succeeds(self):
        """Execute the execute_fib_query method using 5 concurrent requests
        and ensure they all succeed.  The helper method will raise an assert
        if there is a failure retriving any of the concurrent requests.

        NOTE:  I have seen failures when a large number of requests are made
        simultaneously, such as 10-20 requests kicked off.  Suspect the
        requests library may have an issue from the stack trace -- the server
        side seems ok.
        """

        for thread_index in range(99999, 99950, -10):
            request_thread = threading.Thread(
                target=self.execute_concurrent_request,
                args=(str(thread_index),))
            request_thread.start()


if __name__ == '__main__':
    """Main method to setup logging and initiate the test runner."""

    log_file_name = 'fibcli-test.log'
    log_file = open(log_file_name, "w")
    runner = unittest.TextTestRunner(log_file)

    unittest.main(testRunner=runner)

    log_file.close()
