import sys
import ctypes
import os

if sys.platform == 'darwin':
    sofile = 'rdtsc.dylib'
elif sys.platform == 'win32':
    sofile = 'rdtsc.dll'
else:
    sofile = 'rdtsc.so.1'

so = ctypes.CDLL(os.path.join(os.path.dirname(__file__), sofile), use_errno=True)

get_cycles = so.get_cycles
get_cycles.argtypes = []
get_cycles.restype = ctypes.c_ulonglong
