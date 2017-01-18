#/bin/bash

# Setup the commands for our Fibonacci unit test execution.

PYTHON_BIN=python3
FIB_TEST=fibcli-test.py

# Run the tests for the Fibonacci client and capture the overall result.

${PYTHON_BIN} ${FIB_TEST}
TEST_RESULT=$?

# If the test runner returns 0, we successfully executed all our tests.  Any
# other value indicates a bomb or bombs went off somewhere, thusly indicating
# we need to resolve an issue.

if [ "${TEST_RESULT}" -eq "0" ]; then
  echo "PASS"
else
  echo "FAIL"
fi
