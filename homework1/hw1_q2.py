def shift(lst, k, move = "left"):
    if move == "right":
        k = len(lst) - k
    for i in range(k):
        char = lst.pop(0)
        lst.append(char)

    return lst
