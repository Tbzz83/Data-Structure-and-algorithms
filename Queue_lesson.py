wmt_stick_price_queue = []
wmt_stick_price_queue.insert(0,131.10)
wmt_stick_price_queue.insert(0,132.12)
wmt_stick_price_queue.insert(0,135)

print(wmt_stick_price_queue)

wmt_stick_price_queue.pop() # 131.1 'popped' out

print(wmt_stick_price_queue)

# List can work as queue but has problems with dynamic array (memory issues)
# We can use deque from collections module

from collections import deque

q = deque()
q.appendleft(5) # Appends to left hand side as you would expect in a queue
q.appendleft(8)
q.appendleft(27)

q.pop() # 5 popped as it is first in first out

print(q)

# We can create a class called queue using deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val): # Place element in queue
        self.buffer.appendleft(val)

    def deque(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


