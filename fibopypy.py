import time

def fib(n):
  if n == 1 or n == 0:
    return 1
  return fib(n - 1) + fib(n - 2)

t0 = time.time()
fib(35)
t1 = time.time()
print(f"{(t1 - t0) * 1000} ms")
