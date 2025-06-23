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

#Test cases

dq = deque()
dq.append(20)
dq.append(30)
dq.append(340)
print(dq)
print("Size of dq: ", len(dq))
dq.append(20)
print(dq)
dq.append(6)
print(dq)
dq.remove(20) # removes first occurrence of 20 in the list
print(dq)
dq.pop()
print(dq)
print(len(dq))
print(dq.count(20))
print("Is Empty: ",len(dq) == 0)






