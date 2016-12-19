#cocktail sort

def sort(s):
    lower_bound = -1
    upper_bound = len(s) - 1
    swap = True
    while swap:
        swap = False
        lower_bound += 1
        for i in range(lower_bound, upper_bound):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
                swap = True
        if not swap:
            break
        swap= False
        upper_bound -= 1
        for i in range(upper_bound, lower_bound, -1):
            if s[i] < s[i - 1]:
                s[i], s[i - 1] = s[i - 1], s[i]
                swap = True
     return s
