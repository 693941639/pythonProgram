import time
from functools import lru_cache

@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

start = time.time()
print(fib(40))

print(time.time() - start)
