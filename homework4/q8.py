def flat_list(nested_lst, low, high):
    if low == high:
        new_list = []
        if isinstance(nested_lst[low], list):
            temp = flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
            new_list.extend(temp)
        elif isinstance(nested_lst[low], int):
            new_list.append(nested_lst[low])
    else:
        new_list = flat_list(nested_lst, low, high - 1)
        if isinstance(nested_lst[high], list):
            temp = flat_list(nested_lst[high], 0, len(nested_lst[high]) - 1)
            new_list.extend(temp)
        elif isinstance(nested_lst[high], int):
            new_list.append(nested_lst[high])
    return new_list