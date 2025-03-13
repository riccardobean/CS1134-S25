def appearances(s, low, high):
    if low == high:
        dictionary = {}
        temp = s[low]
        dictionary[temp] = 1
    else:
        dictionary = appearances(s, low + 1, high)
        temp = s[low]
        if temp in dictionary:
            dictionary[temp] += 1
        else:
            dictionary[temp] = 1
    return dictionary