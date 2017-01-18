#/bin/sh

# Setup the commands for our Fibonacci server.

PYTHON_BIN=python3
FIB_SERVER=fibserver.py
FIB_SERVER_PORT=8081
SERVER_LOG=fibserver.log

# Fire off the server to listen for clients.

echo "Launching ${FIB_SERVER} on port ${FIB_SERVER_PORT}"

${PYTHON_BIN} ${FIB_SERVER} ${FIB_SERVER_PORT}
