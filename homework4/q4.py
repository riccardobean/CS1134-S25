def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        val = lst[low]
        minimum = list_min(lst, low + 1, high)
        if val < minimum:
            minimum = val
    return minimum