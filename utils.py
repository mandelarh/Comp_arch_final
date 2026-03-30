import time

def measure_time(func):
    start = time.time()
    result = func()
    end = time.time()
    return result, (end - start)