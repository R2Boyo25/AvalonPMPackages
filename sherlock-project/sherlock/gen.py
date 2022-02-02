import sys

binf = sys.argv[1]
filesFolder = sys.argv[2]

with open("sherlock-runner", 'w') as f:
    f.write(f'#!/bin/bash\npython3 "{filesFolder}/sherlock/sherlock.py" "$@"')