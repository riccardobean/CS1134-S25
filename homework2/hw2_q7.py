def findChange(lst01):
    low = 0
    high = len(lst01) - 1
    while low < high:
        mid = (high + low) // 2
        if lst01[mid] == 0:
            low = mid + 1
        if lst01[mid] == 1:
            high = mid
    return low
