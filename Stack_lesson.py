from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        self.reversed_container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def print_stack(self):
        if self.container != None:
            return self.container
        else:
            return self.reversed_container

    def reverse(self):
        while len(self.container) != 0:
            val = self.container.pop()
            self.reversed_container.append(val)
        return self.reversed_container

s = Stack()
s.push(5)
s.push(6)
s.push(7)
print(s.print_stack())
print(s.reverse())




