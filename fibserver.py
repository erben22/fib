# Implementation of a web server API that serves up Fibonacci numbers.
#
# author: R. Cody Erben (erben22@gmail.com)
# date: 01/15/2017
#
# TODO: Study up on Python coding styles and apply here.
# TODO: Add some additional error handling:
#       - Need some handling around the query parameter on the
#         API.  What if it is not supplied for example?

import web
from fibonacci import Fibonacci

# Setup a mapping of endpoints to respective handlers.

urls = (
  '/fibonacci', 'fibonacciHandler'
)

# Fibonacci endpoint handler.  Will expect a parameter to be present
# for the sequence to calcualte, and if present, will create an instance
# of our Fibonacci class to calculate the value and return it to the caller.

class fibonacciHandler:
    def GET(self):
        queryParameters = web.input()
        fibonacci = Fibonacci(int(queryParameters.desiredSequence))
        return fibonacci.calculate()

# Main method that fires up the web application and listens for
# prospective requests from various clients.

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
