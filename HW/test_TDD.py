# -*- coding: cp1251 -*-
import pytest
from time import time
from generator import fib

class cm_timer:
    def __enter__(self):
        self.__time_begin = time()
    def __exit__(self, type, value, traceback):
        print(time() - self.__time_begin)

c = 100000

# тестирование результатов выполнения
def test_fib_1():
    assert [i for i in fib(5)] == [0, 1, 1, 2, 3]
def test_fib_2():
    assert [i for i in fib(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def test_fib_3():
    assert [i for i in fib(0)] == []

# тестирование на ленивые выражение
def test_fib_time_1():
    print("Время выполнения с ленивыми вычислениями")
    with cm_timer():
        temp = fib(c)
    assert list(fib(c)) == [i for i in fib(c)]

def test_fib_time_2():
    print("Время выполнения с обычными вычислениями")
    with cm_timer():
        temp = [i for i in fib(c)]
    assert [i for i in fib(c)] == list(fib(c))

if __name__ == "__main__":
    test_fib_time_1()
    test_fib_time_2()