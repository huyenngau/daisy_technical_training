# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def size(self):
        return self.in_stack.size() + self.out_stack.size()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        # out stack is empty
        if not self.out_stack.items:
            while self.in_stack.items:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size() == 1) else "Fail")