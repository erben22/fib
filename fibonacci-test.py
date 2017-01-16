# Unit tests for the Fibonacci class.
#
# author: R. Cody Erben (erben22@gmail.com)
# date: 01/15/2017
#
# TODO: Study up on Python coding styles and apply here.

import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_calculate(self):
        fibonacci = Fibonacci(7)
        self.assertEqual(fibonacci.calculate(), 13)

# Runner for tests in the TestFibonacci class.

if __name__ == '__main__':
    unittest.main()
