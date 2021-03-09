from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("int fibo(int n);")
ffibuilder.set_source("pyadd",'#include "fibo.h"',sources=["fibo.c"])
ffibuilder.compile()
