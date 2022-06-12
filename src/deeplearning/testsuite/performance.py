import time


def time_measure(func):
    def wrapper(*args, **kwargs):
        t_start = time.time()
        fresult = func(*args, **kwargs)
        t_result = time.time() - t_start
        print("%s(): " % func.__name__, t_result, " ms")
        return fresult

    return wrapper
