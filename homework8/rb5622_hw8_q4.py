def find_min_abs_difference(bst):
    def inorder(root):
        def subtree_inorder(root):
            if root is None:
                return
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)
        yield from subtree_inorder(root)

    prev = None
    lowest = None
    for node in inorder(bst.root):
        curr = node.item.key
        if prev is not None:
            diff = abs(curr - prev)
            if lowest is None or diff < lowest:
                lowest = diff
        prev = curr

    return lowest