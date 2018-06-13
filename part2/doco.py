import time


class Timer(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print("실행시간은 {time}초 입니다.".format(time=(end_time - start_time)))
        return result


def get_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("실행시간은 {time}초 입니다.".format(time=(end_time - start_time)))
        return result

    return wrapper


@get_timer
@Timer
def fibonacci_iterative(n):
    prev_n, cur_n = 0, 1
    i = 1

    while i < n:
        cur_n, prev_n = cur_n + prev_n, cur_n

        i += 1

    return cur_n


@get_timer
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


fibonacci_iterative(200)
# fibonacci_recursive(200)
