""" Implementation of cocktail sort or bidirectional bubble sort. 
    It's also known as happy hour sort. 
    Walk the list bidirectionally, swapping neighbors if one should come
    before/after the other.
    Time Complexity: O(n**2)
    Space Complexity: O(1) Auxiliary
    Stable: Yes
"""

def cocktail_sort(s):
    lower_bound = -1
    upper_bound = len(s) - 1
    swapped = True
    while swapped:
        swapped = False
        lower_bound += 1
        for i in range(lower_bound, upper_bound):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        upper_bound -= 1
        for i in range(upper_bound, lower_bound, -1):
            if s[i] < s[i - 1]:
                s[i], s[i - 1] = s[i - 1], s[i]
                swapped = True
    return s
