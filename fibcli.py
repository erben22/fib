# Command line interface to the fibonacci web service.
# Pass it a desired Fibonacci sequence, and it will output the
# Fibonacci for that number.
#
# author: R. Cody Erben (erben22@gmail.com)
# date: 01/15/2017
#
# TODO: Add some additional error handling:
#       - What if someone passing in a string on the command line?
#       - What if the web server is not available?  Need to look at
#         response.statusCode.
# TODO: Exception handling around requests.get call?
# TODO: Make the server information and port constants (could lead to
#       extending tool to pass those in on the command line in the future).

import sys
import requests


def execute_fib_query(fibonacciSequence):
    url = 'http://localhost:8081/fibonacci'
    requestParameters = {'desiredSequence': int(fibonacciSequence)}

    response = requests.get(url, params=requestParameters)

    return response.text


if __name__ == '__main__':
    if len(sys.argv) == 2:
        fibonacciValue = execute_fib_query(int(sys.argv[1]))

        print(fibonacciValue)
    else:
        print("Please supply the Fibonacci sequence value as an argument")
