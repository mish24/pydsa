from pydsa import comb_sort
from random import randint

def test_comb_sort():
    a = [randint(1, 10) for i in range(10)]
    b = sorted(a)
    comb_sort(a)
    assert a == b

