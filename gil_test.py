import util
import threading

number = 100000000

@util.cal_time
def CountDown(n):
    while n > 0:
        n -= 1

thread_1 = threading.Thread(target=CountDown, args=[number // 2])
thread_2 = threading.Thread(target=CountDown, args=[number // 2])

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
