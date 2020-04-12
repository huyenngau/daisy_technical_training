def check_bst(node, lower, upper):
    """
    Determine wether the input is a binary tree or not

    Args:
       node(object): A BST object
       lower(int):
       upper(int):
    Returns:
       bool: True if it is a BST and False if not
    """
    if node is None:
        return True

    if node.value < lower or node.value > upper:
        return False

    else:
        left_check = check_bst(node.left, lower, node.value - 1)
        right_check = check_bst(node.right, node.value + 1, upper)
        return left_check and right_check


class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


f = Tree(4)
e = Tree(3, None, f)

d = Tree(1)
b = Tree(2, d, e)

c = Tree(6)
a = Tree(5, b, c)

my_tree = a
lower_test = 0
upper_test = 100

print("Pass" if check_bst(my_tree, lower_test, upper_test) else "Fail")
