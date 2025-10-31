from ArrayDeque import ArrayDeque


def permutations(lst):
    deque = ArrayDeque()
    deque.enqueue_last([])
    result = []

    if len(lst) == 0:
        return [[]]

    while not deque.is_empty():
        perm = deque.dequeue_first()
        if len(perm) == len(lst):
            result.append(perm)
        else:
            for num in lst:
                if num not in perm:
                    new_perm = perm[:]
                    new_perm.append(num)
                    deque.enqueue_last(new_perm)
    return result
