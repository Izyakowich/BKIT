from contextlib import *
import time

class cm_timer_1():
    def __enter__(self):
        self.begin = time.time()
    def __exit__(self, type, value, traceback):
        print(time.time() - self.begin)


@contextmanager
def cm_timer_2():
    begin = time.time()
    yield
    print(time.time() - begin)