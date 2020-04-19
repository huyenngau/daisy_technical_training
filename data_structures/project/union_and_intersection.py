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
    llist_1.remove_duplicates()

    intersection_llist = LinkedList()

    node_1 = llist_1.head
    while node_1:
        if llist_2.search(node_1.value) is not None:
            intersection_llist.append(node_1)
        node_1 = node_1.next

    if intersection_llist.head is None:
        raise Exception("Can not get interaction from 2 linked lists")

    intersection_llist.remove_duplicates()
    return intersection_llist


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
