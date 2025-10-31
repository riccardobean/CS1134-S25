from BinarySearchTreeMap import BinartSearchTreeMap

def restore_bst(prefix_lst):
    bst = BinartSearchTreeMap()
    for el in prefix_lst:
        bst.insert(el, None)
    return bst