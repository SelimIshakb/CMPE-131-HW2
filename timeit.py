import time

def calculate_time(func):
    def inner():
        time1 = time.time()
        func()
        time2 = time.time()
        print("Total time", time2 - time1)
    return inner
