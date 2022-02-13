import sys

binf = sys.argv[1]
filesFolder = sys.argv[2]

with open(binf, 'w') as f:
    f.write(f'#!/bin/bash\njava -jar "{filesFolder}/build/libs/cassadra-client-1.0.2-exec.jar" "$@"')