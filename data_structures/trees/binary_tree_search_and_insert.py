class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current_node, new_val):
        if current_node.value == new_val:
            raise Exception("Two nodes with the same value won't be inserted into the tree!")

        new_node = Node(new_val)
        if current_node.value > new_val:
            if current_node.left:
                self.insert_helper(current_node.left, new_val)
            else:
                current_node.left = new_node
        else:
            if current_node.right:
                self.insert_helper(current_node.right, new_val)
            else:
                current_node.right = new_node

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current_node, find_val):
        if current_node:
            if current_node.value == find_val:
                return True
            elif current_node.value > find_val:
                return self.search_helper(current_node=current_node.left, find_val=find_val)
            elif current_node.value < find_val:
                return self.search_helper(current_node=current_node.right, find_val=find_val)
            else:
                raise Exception("Could not find value = {}".format(find_val))
        return False

    def print_tree(self):
        # Print out all tree nodes as they are visited in a pre-order traversal.
        return self.preorder_print(start=self.root, traversal="")[:-1]

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
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print(tree.print_tree())

# Check search
print("Pass" if tree.search(4) else "Fail")
print("Pass" if not tree.search(6) else "Fail")
