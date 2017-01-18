"""Command line interface to the fibonacci web service.
    Pass it a desired Fibonacci sequence, and it will output the
    Fibonacci for that number.

    TODO: Add some additional error handling:
            - What if someone passing in a string on the command line?
            - What if the web server is not available?  Need to look at
              response.statusCode.
    TODO: Exception handling around requests.get call?
    TODO: Make the server information and port constants (could lead to
          extending tool to pass those in on the command line in the future).
"""

import sys
import requests


def execute_fibonacci_query(fibonacci_sequence):
    """Execute a call on the Fibonacci API with the supplied sequence.

    Args:
        fibonacci_sequence (int): Desired Fibonacci sequence to
        retrieve a value for.

    Returns:
        Fibonacci value for the supplied sequence.

    """

    url = 'http://localhost:8080/fibonacci'
    request_parameters = {'desiredSequence': int(fibonacci_sequence)}

    response = requests.get(url, params=request_parameters)

    return response.text


if __name__ == '__main__':
    """Main method to execute the Fibonacci client routine.

    Args:
        sys.argv (array): Collection of arguments from the command line.
    """

    if len(sys.argv) == 2:
        fibonacci_value = execute_fibonacci_query(int(sys.argv[1]))

        print(fibonacci_value)
    else:
        print("Please supply the Fibonacci sequence value as an argument")
