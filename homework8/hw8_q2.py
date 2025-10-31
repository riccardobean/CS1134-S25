from BinarySearchTreeMap import BinartSearchTreeMap

def create_chain_bst(n):
    bst = BinartSearchTreeMap()
    for i in range(1, n+1):
        bst.insert(i, None)
    return bst

def create_complete_bst(n):
    bst = BinartSearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low > high:
        return
    else:
        root_data = (high + low) // 2
        bst.insert(root_data, None)
        add_items(bst, low, root_data - 1)
        add_items(bst, root_data + 1, high)
