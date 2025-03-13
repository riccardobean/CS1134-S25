def split_by_sign(lst, low, high):
    if low == high:
        return
    else:
        if low < high and lst[low] < 0:
            low += 1
        if low < high and lst[high] > 0:
            high -= 1
        if low < high and lst[low] > 0 and lst[high] < 0:
            lst[low], lst[high] = lst[high], lst[low]
        split_by_sign(lst, low, high)