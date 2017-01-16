# fib
Fibonacci number generator implemented in a client/server fashion.

- python3 -m pip install web.py==0.40.dev0
- python3 -m pip install requests

- Application uses port 8080 on localhost by default.
  - Run with python3 fibserver.py 8081 to run on a different port.
  - Run client with python3 fibcli.py 7 where the argument is the Fibonacci
    sequence one wishes to see the value for.
