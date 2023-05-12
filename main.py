import json
import sys
import os
from assembler import Assembler
from emulator import Emulator

fileName = 'test.mas'
if len(sys.argv) > 1:
    fileName = sys.argv[1]

if not os.path.exists(fileName):
    print(f'Error: file "{fileName}" not found')
    exit(1)

code = []
with open(fileName, 'r') as f:
    code = Assembler.run(f.readlines(), doPrints = False)

Emulator.run(code)


# fix this nik
#if '--run' in sys.argv:
#    import subprocess
#    subprocess.run([sys.executable, 'emulator.py', dump_fileName], shell=True)