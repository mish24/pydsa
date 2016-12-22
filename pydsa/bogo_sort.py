"""
    bogo_sort.py
    Implementation of bogo sort on a list and returns a sorted list.
    A naive sorting that picks two elements at random and swaps them.
    Time Complexity: O(n * n!)
    Space Complexity: O(1) Auxiliary
    Stable: No
    WARNING: This algorithm may never sort the list correctly.
"""

import random


def bogo_sort(seq):
    if len(seq) == 1:
        return seq
    random.seed()
    while not is_sorted(seq):
        if len(seq) == 2:
            i = 0
            j = 1
        else:
            i = random.randint(0, len(seq) - 2)
            j = random.randint(i, len(seq) - 1)
        seq[i], seq[j] = seq[j], seq[i]
    return seq

"""
As mentioned, this algorithm is not stable. Hence I thought it's important to define a function to check for the same
"""
def is_sorted(seq):
    return all(seq[i - 1] <= seq[i] for i in range(1, len(seq)))
"""
a=[1,5,6,2,4,8]
bogo_sort(a)
print(a)
"""
