# No, Python is not slower than Node

following are the ways to achieve better speed in the python, with or without ffi.

### nodejs
108.26432800013572 ms



### CPython3
2373.1770515441895 ms


### CPython3 with Numba JIT
175.5959987640381 ms


### CPython with LRU cache
0.013589859008789062 ms

### PyPy3
319.6985721588135 ms


### C FFI
21.827220916748047 ms


## misc
rust-python didn't finish the execution since it's a new project there are bugs in it.
that's why keeping the code commented. planning to add one pyo3 version too

