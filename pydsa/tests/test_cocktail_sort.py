from pydsa import cocktail_sort
from random import randint


def test_cocktail_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert cocktail_sort(a) == sorted(b)
