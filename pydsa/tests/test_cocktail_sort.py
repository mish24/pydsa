from pydsa import cocktail_sort
from random import randint

def test_cocktail_sort():
   a= [randint(1,10) for i in range(10)]
   b=sorted(a)
   cocktail_sort(a)
   assert a==b

