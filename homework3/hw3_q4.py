def remove_all(lst, value):
    j = 0
    count = 0
    for i in range(len(lst)):
        if lst[i] != value:
            lst[j] = lst[i]
            j += 1
        else:
            count += 1
    for i in range(count):
        lst.pop()
