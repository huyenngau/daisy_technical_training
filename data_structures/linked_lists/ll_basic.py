# Basic Node and pretty tedious
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)
head.next.next = Node(4)

print(head.value)
print(head.next.value)
print(head.next.next.value)


def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


print_linked_list(head)


