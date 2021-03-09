import time

def fib(n):
  if  n == 0 or n == 1:
    print("iteration", n)
    return 1
  return fib(n - 1) + fib(n - 2)
t0 = time.time()
fib(10)
t1 = time.time()
print(f"{(t1 - t0) * 1000} ms")