class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        # Return True if the value is in the tree, return False otherwise.
        return self.preorder_search(start=self.root, find_val=find_val)

    def print_tree(self):
        # Print out all tree nodes as they are visited in a pre-order traversal.
        return self.preorder_print(start=self.root, traversal="")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start is not None:
            if start.value == find_val:
                return True

            left_node = start.left
            right_node = start.right
            return self.preorder_search(left_node, find_val) or self.preorder_search(right_node, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start is not None:
            traversal += (str(start.value) + '-')

            left_node = start.left
            right_node = start.right
            traversal = self.preorder_print(left_node, traversal)
            traversal = self.preorder_print(right_node, traversal)

        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
print("Pass" if tree.search(4) else "Fail")
print("Pass" if not tree.search(6) else "Fail")
print(tree.print_tree())
print("Pass" if (tree.print_tree() == '1-2-4-5-3') else "Fail")
