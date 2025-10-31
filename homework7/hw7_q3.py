def is_height_balanced(bin_tree):
    def subtree_is_height_balanced(root):
        if root is None:
            return 0, True

        height_left, balance_left = subtree_is_height_balanced(root.left)
        height_right, balance_right = subtree_is_height_balanced(root.right)

        if balance_left and balance_right and -1 <= height_right - height_left <= 1:
            balance = True
        else:
            balance = False

        return 1 + max(height_left, height_right), balance

    if bin_tree is None:
        raise Exception("The tree does not exist")

    height, balance = subtree_is_height_balanced(bin_tree.root)
    return balance
