#/bin/bash

MODULES_LIST=(requests web.py==0.40.dev0)

for MODULE in ${MODULES_LIST[@]}; do
  python3 -m pip install ${MODULE}
done
