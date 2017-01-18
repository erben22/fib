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

## Module:

- Setup script:
 - `./setup-fib-modules.sh`
- web.py: Provides a simple web endpoint handler for API requests for the Fibonacci server.
 - Installation: `python3 -m pip install web.py==0.40.dev0`
- requests: Provides the Fibonacci client with a simple framework for HTTP requests (grass fed, non-GMO, too).
 - Installation: `python3 -m pip install requests`

## Notes

### Server

- Application uses port 8080 on localhost by default.
  - Run with `python3 fibserver.py 8081` to run on a different port.
- Run the included `runserver.sh` script to launch the Fibonacci server.

### Client

- Run client with `python3 fibcli.py 7` where the argument is the Fibonacci sequence one wishes to obtain the value for.
- Run the includes `test.sh` script to execute a series of tests
