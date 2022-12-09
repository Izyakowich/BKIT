import pytest
from main import get_roots

def tests_get_roots_one():
    temp = get_roots(1, 1, 0)
    assert temp == {0}
    temp = get_roots(5, 15, 0)
    assert temp == {0}
    temp = get_roots(30, 18, 0)
    assert temp == {0}

def tests_get_roots_two():
    temp = get_roots(3, -5, -28)
    assert temp == {2, -2}
    temp = get_roots(3, -14, -117)
    assert temp == {3, -3}
    temp = get_roots(11, -86, -117)
    assert temp == {3, -3}

def tests_get_roots_three():
    temp = get_roots(1, -9, 0)
    assert temp == {-3, 0, 3}
    temp = get_roots(3, -75, 0)
    assert temp == {-5, 0, 5}
    temp = get_roots(7, -112, 0)
    assert temp == {-4, 0, 4}

