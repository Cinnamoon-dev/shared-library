from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./lib.so')

ffi.cdef("""
    void showNumbers(int n1, int n2);
    void subNumbers(int n1, int n2);
""")

lib.showNumbers(1, 2)
lib.subNumbers(17, 4)