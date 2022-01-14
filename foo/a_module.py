from functools import wraps
import time

def timefn(fn):
    "A function decorator to measure the time consuming."
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args,**kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2- t1} seconds")
        return result 
    return measure_time

@timefn
def func():
    print("This is module a.")


class Person():
    def __init__(self, weights, heights):
        self.weights = weights
        self.heights = heights

    def get_bmi(self):
        return self.weights*self.heights

    def eghhhkijigtjigjitjgijtgitjgigj(self):
        return "lone too lines"