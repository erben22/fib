"""Implementation of a web server API that serves up Fibonacci numbers.

    TODO: Add some additional error handling:
        - Need some handling around the query parameter on the
          API.  What if it is not supplied for example?
"""

import web
from fibonacci import Fibonacci

urls = (
    '/fibonacci', 'FibonacciHandler'
)
"""Definition of the API endpoint to HTTP handler class."""


class FibonacciHandler:
    """Fibonacci endpoint handler.  Will expect a parameter to be present
        for the sequence to calcualte, and if present, will create an
        instance of our Fibonacci class to calculate the value and return
        it to the caller.
    """

    def GET(self):
        """Implementation of the GET handler interface."""

        query_parameters = web.input()
        fibonacci = Fibonacci(int(query_parameters.desired_sequence))
        return fibonacci.calculate()

if __name__ == "__main__":
    """Main method that fires up the web application and listens for
        prospective requests from various clients.
    """

    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
