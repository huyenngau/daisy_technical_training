class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search(self, value):
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

    def remove_duplicates(self):
        current_node = self.head
        element_list = []
        previous_node = None
        while current_node:
            if current_node.value not in element_list:
                element_list.append(current_node.value)
                previous_node = current_node
                current_node = current_node.next
            else:
                previous_node.next = current_node.next
                current_node = current_node.next


def union(llist_1, llist_2):
    llist_1.remove_duplicates()
    llist_2.remove_duplicates()

    union_llist = LinkedList()

    node_1 = llist_1.head
    while node_1:
        union_llist.append(node_1)
        node_1 = node_1.next

    node_2 = llist_2.head
    while node_2:
        if llist_1.search(node_2.value) is None:
            union_llist.append(node_2)
        node_2 = node_2.next

    return union_llist


def intersection(llist_1, llist_2):
    intersection_llist = LinkedList()
    node_1 = llist_1.head
    while node_1:
        if llist_2.search(node_1.value) is not None:
            intersection_llist.append(node_1)
        node_1 = node_1.next

    if intersection_llist.head is None:
        return None

    return intersection_llist


def test_function(arr_1, arr_2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in arr_1:
        linked_list_1.append(i)

    for i in arr_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


# Test case 1
print("-------------------------------------------------------------------")
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
# union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
# intersection: 4 -> 6 -> 21 ->
test_function(element_1, element_2)
print("-------------------------------------------------------------------")

# Test case 2
element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_4 = [1, 7, 8, 9, 11, 21, 1]
# union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
# intersection: None
test_function(element_3, element_4)
print("-------------------------------------------------------------------")

# Test case 3
element_5 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_6 = [1, 7, 8, 9, 11, 21, 1]
# union: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
# intersection: None
test_function(element_5, element_6)
print("-------------------------------------------------------------------")

