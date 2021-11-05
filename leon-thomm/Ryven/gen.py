import sys, os, shutil

binf = sys.argv[1]
filesFolder = sys.argv[2]

with open('ryven', 'w') as f:
    f.write(f'#!/bin/bash\npython3 "{filesFolder}/Ryven/src/Ryven.py" "$@"')