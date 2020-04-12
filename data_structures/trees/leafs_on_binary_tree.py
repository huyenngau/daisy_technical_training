def count_binary_tree_leafs(tree):
    """
    Find the number of leafs on a binary tree

    Args:
       tree(object): Input binary tree
    Returns:
       int: The number of leafs of the tree
    """
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    else:
        return count_binary_tree_leafs(tree.left) + count_binary_tree_leafs(tree.right)


class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


f = Tree("F")
e = Tree("E", None, f)

d = Tree("D")
b = Tree("B", d, e)

c = Tree("C")
a = Tree("A", b, c)

my_tree = a
print("Pass" if (3 == count_binary_tree_leafs(my_tree)) else "Fail")