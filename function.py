# add_fnc = lambda x: x + 1

# print(add_fnc(1))

# def foo(ni: int) -> int:
#     return ni

# print("str")

# def fooo(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)

# fooo(arg3="one", arg1="two", arg2="three")


# def fnc(arg1, *arg2, **arg3):
#     '''
#     Description for fnc
#     '''
#     print(f"arg1={arg1}, arg2={arg2}, arg3={arg3}")

# print(dir(fnc))
# print(fnc.__dir__)

# def fnc(*arg_noname, **arg_name):
#     print(f"arg nums is:{len(arg_noname) + len(arg_name)} {arg_noname} {arg_name}")
# fnc(1, 2, 3, 4, arg1="one", arg2="two", arg3="three")

# def fnc(a):
    # return a * a
# def mymap(fc, a):
#     return fc(a)
# print(mymap(fnc, 2))
# print(tuple(map(fnc, range(5))))
# print(list(map(lambda x: x * x, range(5))))
# print(tuple(filter(lambda x: x % 2 == 0, range(20))))
# print(filter(lambda x: x % 2 == 0, range(20)))

# from functools import reduce, partial
# print(reduce(lambda x, y: x + y, range(20)))
# int_16_2_10 = partial(int, base=16)
# print(int_16_2_10("1f"))

import time
from functools import wraps

def exec_time(func):
    @wraps(func)
    def wrapper(a):
        start = time.time()
        func(a)
        print(f"Executing time is {time.time() - start}")
    return wrapper

@exec_time
def func1(a):
    return a * a * a
        
func1(10000)


print(func1.__name__)
