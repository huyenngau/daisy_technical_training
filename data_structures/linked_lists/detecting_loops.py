class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return


def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    if linked_list.head is None:
        return False

    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while slow_runner.next and fast_runner.next:
        if slow_runner.next == slow_runner:
            return True

        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        if slow_runner == fast_runner:
            return True
    return False


# Test Cases

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next
node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

print("Pass" if (iscircular(list_with_loop) is True) else "Fail")

linked_list_test_case_2 = LinkedList([-4, 7, 2, 5, -1])
print("Pass" if (iscircular(linked_list_test_case_2) is False) else "Fail")
print("Pass" if (iscircular(LinkedList([1])) is False) else "Fail")
