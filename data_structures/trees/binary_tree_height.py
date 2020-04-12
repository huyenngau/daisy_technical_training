def binary_tree_height(tree):
    """
    Find the height of a binary tree

    Args:
       tree(object): Input binary tree
    Returns:
       int: The height of the tree
    """

    if tree is None:
        return 0

    else:
        height_left = 0
        height_right = 0
        if tree.left is not None:
            height_left = 1 + binary_tree_height(tree.left)

        if tree.right is not None:
            height_right = 1 + binary_tree_height(tree.right)

    return max(height_left, height_right)


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

my_tree_1 = a
my_tree_2 = f

print("Pass" if (3 == binary_tree_height(my_tree_1)) else "Fail")
print("Pass" if (0 == binary_tree_height(my_tree_2)) else "Fail")