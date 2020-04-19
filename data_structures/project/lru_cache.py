"""
We'll set up our linked list with the most-recently used item at the head of the list
and the least-recently used item at the tail.
In general, finding an item in a linked list is O(n) time, since we need to walk the whole list.
We use a hash map that maps items to linked list nodes.
That lets us find an element in our cache's linked list in O(1)O(1) time, instead of O(n).
"""


class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    # Initialize class variables
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.node_map = {}  # map a key to a Node (explained above)
        self.head = None  # Node with the most recently used key
        self.tail = None  # Node with the least recently used key

    # helper: add node to the head of the doubled linked list
    def add_to_head(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # helper: delete node out of the doubled linked list
    def delete_node(self, node):
        if node is self.head:
            self.head = self.head.next

        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

        if node is self.tail:
            self.tail = self.tail.prev

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.node_map:
            return self.node_map[key].value   # node_map[key].value return a value of that node
        else:
            return -1

    def put(self, key, value):
        if key in self.node_map:
            self.node_map[key].value = value
            self.add_to_head(self.node_map[key])
        else:
            # insert new node to hash_map
            new_node = DoubleNode(key, value)
            self.node_map[key] = new_node

            if self.size < self.capacity:
                self.add_to_head(new_node)
                self.size += 1

            else:
                if self.size == self.capacity:
                    key = self.tail.key  # get key of least recently used node
                    self.delete_node(self.tail)  # delete node out of double linked list
                    del self.node_map[key]  # delete key out of hash_map
                    self.add_to_head(new_node)


# Test case
our_cache = LRU_Cache(5)

our_cache.put(1, 1)
our_cache.put(2, 2)
our_cache.put(2, 8)
our_cache.put(3, 3)
our_cache.put(4, 4)


print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.put(5, 5)
our_cache.put(6, 6)

print(our_cache.get(1))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("-----------")
print("Our cache: ")
node = our_cache.head
while node:
    print(node.value)
    node = node.next
