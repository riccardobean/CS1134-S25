def two_sum(srt_lst, target):
    low = 0
    high = len(srt_lst) - 1
    while low < high:
        if srt_lst[low] + srt_lst[high] == target:
            return low, high
        elif srt_lst[low] + srt_lst[high] < target:
            low += 1
        else:
            high -= 1
    return None