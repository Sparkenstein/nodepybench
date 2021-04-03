import time

def fib(n):
  if n == 1 or n == 0:
    return 1
  return fib(n - 1) + fib(n - 2)

def fib2(nterms):
  n1, n2 = 0, 1
  count = 0
  while count < nterms:
      nth = n1 + n2
      # update values
      n1 = n2
      n2 = nth
      count += 1
  return n2

t0 = time.time()
fib(35)
t1 = time.time()
print(f"{(t1 - t0) * 1000} ms")
