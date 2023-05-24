#pythran export fib(int)

# def fib(n: int) -> int:
#     def fib_helper(n):
#         if n < 2:
#             return n
#         return fib_helper(n - 1) + fib_helper(n - 2)
#     return fib_helper(n)

def fib(n: int) -> int:
    if n < 2:
            return n
    return fib(n - 1) + fib(n - 2)
