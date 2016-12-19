from pydsa import bogo_sort
from random import randint


def test_bogo_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert bogo_sort(a) == sorted(b)
