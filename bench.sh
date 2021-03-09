echo ###############
echo running node
node fibo.js
echo "\n"
echo ###############

echo running CPython3
python fibo.py
echo "\n"
echo ###############


echo running CPython3 with Numba JIT
python fiboJIT.py
echo "\n"
echo ###############


echo running PyPy3
pypy3 fibopypy.py
echo "\n"
echo ###############


# echo running RustPython
# rustpython fiborustpython.py
# echo "\n"
# echo ###############

echo running C FFI
cd cffi
python fiboc.py
echo "\n"
echo ###############

echo ###############