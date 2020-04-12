def lowest_common_ancestor(tree, val_1, val_2):
    """
    Determine the lowest common ancestor

    Args:
       tree(object): A Binary tree object
       val_1(int): A value of a node in Binary tree
       val_2(int): A value of a node in Binary tree
    Returns:
       int: Lowest shared ancestor
    """
    # If the tree is empty, then return None
    if tree is None:
        return None

    # if val_1 and val_2 both are same as root, then return root
    if val_1 == tree.value or val_2 == tree.value:
        return tree.value

    # LCA of left subtree of the root using val_1 and val_2
    left_lca = lowest_common_ancestor(tree.left, val_1, val_2)

    # LCA of right subtree of the root using val_1 and val_2
    right_lca = lowest_common_ancestor(tree.right, val_1, val_2)

    # if left_lca and right_lca are None, then return None
    if left_lca is None and right_lca is None:
        return None

    # if left_lca and right_lca both are non-zero, then return root
    if left_lca is not None and right_lca is not None:
        return tree.value

    # return left OR right
    if left_lca is None:
        return right_lca
    else:
        return left_lca


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
print(lowest_common_ancestor(my_tree, 1, 3))
print(lowest_common_ancestor(my_tree, 6, 4))
print(lowest_common_ancestor(my_tree, 3, 4))
print(lowest_common_ancestor(my_tree, 31, 42))

print("Pass" if 2 == lowest_common_ancestor(my_tree, 1, 3) else "Fail")
