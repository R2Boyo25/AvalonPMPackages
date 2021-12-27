import sys

binf = sys.argv[1]
filesFolder = sys.argv[2]

with open('ryven-runner', 'w') as f:
    f.write(f'#!/bin/bash\npython3 "{filesFolder}/ryven/main/Ryven.py" "$@"')