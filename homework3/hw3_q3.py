def find_duplicates(lst):
    found = [0] * len(lst)
    duplicates = []
    for el in lst:
        found[el] += 1
    for i in range(len(found)):
        if found[i] >= 2:
            duplicates.append(i)
    return duplicates
