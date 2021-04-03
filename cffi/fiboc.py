from pyadd.lib import fibo
import time

t0 = time.time()
fibo(35)
t1 = time.time()
print(f"{(t1 - t0) * 1000} ms")
