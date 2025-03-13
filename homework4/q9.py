def permutations(lst, low, high):
    if low == high:
        return [lst[low:high+1]]
    else:
        perms = permutations(lst, low + 1, high)
        ret_list = []

        for perm in perms:
            for index in range(len(perm) + 1):
                temp = perm[:]
                temp.insert(index, lst[low])
                ret_list.append(temp)
        return ret_list