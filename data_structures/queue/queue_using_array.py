class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0] * initial_size
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        if self.next_index + 1 == len(self.arr):
            self._handle_queue_capacity_full()
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None
        front_element = self.front()
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return front_element

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.arr[self.front_index]

    def _handle_queue_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(len(self.arr) * 2)]
        for index, element in enumerate(old_arr):
            self.arr[index] = element


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
