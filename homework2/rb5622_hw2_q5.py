def split_parity(lst):
    low = 0
    high = len(lst) - 1
    while low < high:
        if lst[low] % 2 == 0 and lst[high] % 2 != 0:
            lst[low], lst[high] = lst[high], lst[low]
            low += 1
            high -= 1
        else:
            if lst[low] % 2 != 0:
                low += 1
            if lst[high] % 2 == 0:
                high -= 1