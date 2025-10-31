from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    exp_list = prefix_exp_str.split()

    def create_expression_subtree(index):
        char = exp_list[index]

        if char in '+-*/':
            left_node, next_index = create_expression_subtree(index + 1)
            right_node, last_index = create_expression_subtree(next_index)
            root = LinkedBinaryTree.Node(char, left_node, right_node)
            return root, last_index
        else:
            return LinkedBinaryTree.Node(int(char)), index + 1

    root_node, size = create_expression_subtree(0)
    tree = LinkedBinaryTree()
    tree.root = root_node
    return tree


def prefix_to_postfix(prefix_exp_str):
    def postorder(root):
        if root is None:
            return ""
        else:
            left = postorder(root.left)
            right = postorder(root.right)
            return f"{left}{right}{root.data} "
    tree = create_expression_tree(prefix_exp_str)
    return postorder(tree.root).strip()

from LinkedBinaryTreeHelper import display_tree
print("\nExpression Tree for '* 2 + - 15 6 4':")
exp_tree = create_expression_tree("* 2 + - 15 6 4")
display_tree(exp_tree.root)
