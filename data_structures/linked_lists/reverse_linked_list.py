# Helper Code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    reserve_llist = LinkedList()  # reserve_llist.head = None
    node = linked_list.head  # node.value = linked_list.head.value
    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to
    # the new linked list
    while node:
        old_head = reserve_llist.head
        new_node = node
        node = node.next
        new_node.next = old_head

        reserve_llist.head = new_node

    return reserve_llist


llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)

reserve_ll = reverse(llist)
node = reserve_ll.head
while node:
    print(node.value)
    node = node.next

print("Pass" if (llist == reverse(llist)) else "Fail")
