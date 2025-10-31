def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        lowest = root.data
        highest = root.data

        if not root.left is None:
            left_lowest, left_highest = subtree_min_and_max(root.left)
            lowest = min(left_lowest, lowest)
            highest = max(left_highest, highest)

        if not root.right is None:
            right_lowest, right_highest = subtree_min_and_max(root.right)
            lowest = min(right_lowest, lowest)
            highest = max(right_highest, highest)

        return lowest, highest

    if bin_tree is None:
        raise Exception("Tree is None")
    if bin_tree.root is None:
        raise Exception("Tree is empty")
    return subtree_min_and_max(bin_tree.root)