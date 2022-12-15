import pytest

from main import *

def test_1():
    temp = Task_1(one_to_many)

    assert temp[0] == ('ASUS ROG', 120000, 'киберспортивный класс')
    assert temp[1] == ('ASUS TUF', 100000, 'киберспортивный класс')
    assert temp[2] == ('Asus Vivobook', 70000, 'просто класс')
    assert temp[3] == ('MacBook Air m1', 80000, 'яблочный класс')
    assert temp[4] == ('MacBook Air m2', 110000, 'яблочный класс')

def test_2():
    temp = Task_2(one_to_many)
    assert temp[0] == ('киберспортивный класс', 220000)
    assert temp[1] == ('яблочный класс', 190000)
    assert temp[2] == ('просто класс', 70000)

def test_3():
    temp = Task_3(one_to_many)
    assert temp == {'киберспортивный класс': ['ASUS ROG', 'ASUS TUF'], 'яблочный класс': ['MacBook Air m1', 'MacBook Air m2']}