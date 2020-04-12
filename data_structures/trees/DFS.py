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


def print_tree_preorder(tree):
    """
    Implement a pre-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """
    if tree is None:
        return
    print(tree, end=' ')
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)


print("Pre-order:", end=' ')
print_tree_preorder(my_tree)


def print_tree_inorder(tree):
    """
    Implement a in-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """

    if tree is None:
        return
    print_tree_inorder(tree.left)
    print(tree, end=' ')
    print_tree_inorder(tree.right)


print("In-order:", end=' ')
print_tree_inorder(my_tree)


def print_tree_postorder(tree):
    """
    Implement a post-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """

    if tree is None:
        return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree, end=' ')


print("Post-order:", end=' ')
print_tree_postorder(my_tree)