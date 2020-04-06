class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, element):
        self.arr[self.next_index] = element
        self.next_index += 1
        self.num_elements += 1


foo = Stack()
foo.push(["Test!", "ab"])
print(foo.arr)
print("Pass" if foo.arr[0] == ["Test!", "ab"] else "Fail")