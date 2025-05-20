import time

def efficiency_measure(func, args):
    """Returns result and time taken for algorithm to finish """
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return [result, round(end_time - start_time, 2)]

