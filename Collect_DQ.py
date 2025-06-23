"""Use Python's collections.deque to implement a more efficient queue.
Instructions:
Implement a class DequeQueue with the following methods:
enqueue(item): Adds an item to the end of the queue.
dequeue(): Removes and returns the item at the front of the queue. If the queue is empty,
it should raise an exception.
is_empty(): Returns True if the queue is empty, False otherwise.
size(): Returns the number of items in the queue.
Write a few test cases to demonstrate the functionality of the queue."""

from collections import deque

class DequeQueue:
    def __init__(self):
        # Initializing an empty deque
        self._queue = deque()

    def enqueue(self, value):
        self._queue.append(value)

    def is_empty(self):
        return len(self._queue) == 0  # returns True if length is zero else false

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue, can't dequeue")
        return self._queue.pop()

    def size(self):  # return the number of items in the linked list
        return len(self._queue)

    def __repr__(self):
        return f"{list(self._queue)}"

# Test cases
if __name__ == "__main__":
    dq = DequeQueue()
    print(dq.is_empty())
    dq.enqueue(1)
    dq.enqueue(2)
    dq.enqueue(3)
    dq.enqueue(4)
    print(dq)
    print(dq.is_empty())
    print(dq.size())
    print(dq.dequeue())
    print(dq)
