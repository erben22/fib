# fib

Fibonacci number generator implemented in a client/server fashion.

## Requirements:

Python Version:  3.6.0

### Modules:

- web.py
 - `python3 -m pip install web.py==0.40.dev0`
- requests
 - `python3 -m pip install requests`

## Notes

### Server

- Application uses port 8080 on localhost by default.
  - Run with `python3 fibserver.py 8081` to run on a different port.
- Run the included `runserver.sh` script to launch the Fibonacci server.

### Client

- Run client with `python3 fibcli.py 7` where the argument is the Fibonacci sequence one wishes to obtain the value for.
- Run the includes `test.sh` script to execute a series of tests
