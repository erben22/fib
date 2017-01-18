#/bin/bash

# Run pep8 to inspect our code and ensure it meets the standard.

pep8 *.py
PEP8_RESULT=$?

if [ "${PEP8_RESULT}" -eq "0" ]; then
  echo "PASS:  All source files meet PEP8 guidelines."
else
  echo "FAIL: Issues with PEP8 guidelines detected."
fi
