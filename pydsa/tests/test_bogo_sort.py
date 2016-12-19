from pydsa import bogo_sort
from random import randint


def test_bogo_sort():
    a = [randint(1, 10) for i in range(10)]
    b = sorted(a)
    bogo_sort(a)
    assert a == b

