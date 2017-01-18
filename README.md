# fib

Fibonacci number generator implemented in a client/server fashion.

## Requirements:

- Python Version 3.6.0

## Usage:

- Run `./setup-fib-modules.sh` to install required modules.
- Run `./runserver.sh` to launch the Fibonacci API server.
- Run `./test.sh` to run a series of tests on the Fibonacci API server using the
Fibonacci client (the Fibonacci server must already be running!).

- Other fun executions:
 - `python3 fibcli.py 4`
  - Returns the Fibonacci value for the user supplied Fibonacci sequence.
 - `python3 fibonacci-test.py`
  - Execute unit tests on the Fibonacci class.
 - `./validate-pep8.sh`
  - Runs validation on the source code against PEP8 guidelines.

## Module:

- Setup script (will install all the listed modules below automatically):
 - `./setup-fib-modules.sh`
- web.py: Provides a simple web endpoint handler for API requests for the Fibonacci server.
 - Installation: `python3 -m pip install web.py==0.40.dev0`
- requests: Provides the Fibonacci client with a simple framework for HTTP requests (grass fed, non-GMO, too).
 - Installation: `python3 -m pip install requests`
- pep8: (Optional).  Allows for the validate-pep8.sh script to validate code style according to PEP8 guidelines.
 - Installation: `python3 -m pip install pep8`

## Notes

### Server

- Application uses port 8080 on localhost by default.
  - Run with `python3 fibserver.py 8081` to run on a different port.
- Run the included `runserver.sh` script to launch the Fibonacci server.

### Client

- Run client with `python3 fibcli.py 7` where the argument is the Fibonacci sequence one wishes to obtain the value for.
- Run the includes `test.sh` script to execute a series of tests

### Tests

- Tests run in the `./test.sh` script exercise several scenarios:
 - Test with a valid sequence and ensure correct results is returned.
 - Test with a 0 sequence and ensure 0 is returned for the value.
 - Test with a negative number and ensure a failure occurs.
 - Test with a non-numeric value and ensure a failure occurs
 - Test a larger value (1234) and ensure the correct value is returned.
 - Test a much larger value (1234567) and ensure a non-zero value is returned.
 - Spin up 5 concurrent requests and ensure they are successfully serviced without error.

### Fibonacci Values Supported
- The current implementation, while not a pretty nor optimized version, will retrieve a Fibonacci values for the following inputs in the approximate times below:
 - 99,999:    0.2s 
 - 999,999:   15s
 - 3,000,000: 144s 