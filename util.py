import time
import functools

def cal_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("Exec time is ", time.time() - start)
    return wrapper
