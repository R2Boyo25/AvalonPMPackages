import sys

binf = sys.argv[1]
filesFolder = sys.argv[2]

with open(binf, 'w') as f:
    f.write(f'#!/bin/bash\njava -jar "{filesFolder}/build/libs/cassadra-client-0.0.0-0-exec.jar" "$@"')