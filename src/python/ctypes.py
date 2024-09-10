import ctypes

lib = ctypes.CDLL('./lib.so')

lib.showNumbers.restype = None
lib.showNumbers.argtypes = [ctypes.c_int, ctypes.c_int]

lib.showNumbers(1, 3)
