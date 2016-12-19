from pydsa import comb_sort
from random import randint

def test_comb_sort():
  a = b = [randint(1, 100) for i in range(100)]
    assert cocktail_sort(a) == sorted(b)
