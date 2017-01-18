# Test cases for the Fibonacci client using the unittest framework.
#
# author: R. Cody Erben (erben22@gmail.com)
# date: 01/17/2017

import unittest
from fibcli import execute_fib_query


class TestFibonacciCli(unittest.TestCase):

    def test_execute_fib_query_succeeds_simple(self):
        self.assertEqual(execute_fib_query(7), str(13))

# Runner for tests in the TestFibonacciCli class.

if __name__ == '__main__':
    # Setup the test runner to output text results to a log file:

    logFileName = 'fibcli-test.log'
    logFile = open(logFileName, "w")
    runner = unittest.TextTestRunner(logFile)

    unittest.main(testRunner=runner)

    logFile.close()
