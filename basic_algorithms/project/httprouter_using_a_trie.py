from collections import defaultdict


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children and a handler
        self.handler = handler
        self.children = defaultdict(RouteTrieNode)

    def insert(self, node):
        # Insert the node
        return self.children[node]


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, paths, handler):
        # Similar to our previous example, recursively add nodes
        # assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for path in paths:
            node = node.insert(path)

        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler
        current_node = self.root

        if path == [""]:
            return self.root.handler

        for child_path in path:
            current_node = current_node.children[child_path]

        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # Add a handler for 404 page not found responses
        self.root = RouteTrie(root_handler)
        self.not_found = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # Split the path and pass the pass parts as a list to the RouteTrie
        child_paths = split_path(path)
        self.root.insert(child_paths, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # return the "not found" handler if it's not found or
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        child_paths = split_path(path)
        handler = self.root.find(child_paths)
        if handler:
            return handler
        else:
            return self.not_found


def split_path(path):
    # Need to split the path into parts for
    # both the add_handler and lookup functions,
    child_paths = path.split("/")
    if path.endswith("/"):
        return child_paths[:-1]
    return child_paths


# Here are some test cases and expected outputs

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'
