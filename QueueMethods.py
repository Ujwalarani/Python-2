"""Implement a basic queue using Python's built-in list data structure.
The queue should support standard operations like enqueue, dequeue, and checking if the queue is empty.
Instructions:
Implement a class  Queue with the following methods:
enqueue(item): Adds an item to the end of the queue.
dequeue(): Removes and returns the item at the front of the queue. If the queue is empty,
it should raise an exception.
is_empty(): Returns True if the queue is empty, False otherwise.
size(): Returns the number of items in the queue.
Write a few test cases to demonstrate the functionality of the queue."""

# Define Class Queue
class Queue:
    def __init__(self):
        # create an empty queue to store the queue items
        self.item = []
    # Method to add an item to the end of the queue
    def enqueue(self, item):
        # Using append method to add the items to the end of the queue
        self.item.append(item)
    # Method to check if the queue has items or not
    def is_empty(self):
        # we need to check length of the queue to find if the queue is empty or not
        # Below we are checking is length of queue is zero
        return len(self.item) == 0
    # Method to remove an item from the queue
    def dequeue(self):
        # check first if teh queue is empty or not using the function defined above
        if self.is_empty():
            raise IndexError("Nothing to Dequeue as queue is empty")
        # to remove item for the index specified use pop method
        return self.item.pop(0)
    def size(self):
        # Check the length of the queue
        return len(self.item)

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for item in self.item:
            print(item)


q = Queue()

print("Is queue empty?", q.is_empty())

q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("List of items added to queue")
q.print_queue()

print("Queue size after adding:", q.size())

print("Dequeue item:", q.dequeue())

print("Is the queue empty?", q.is_empty())

print("Queue size after dequeue:", q.size())

print("Dequeue item:", q.dequeue())
print("Dequeue item:", q.dequeue())
print("Queue size after dequeue:", q.size())
print("Is the queue empty?", q.is_empty())

q.print_queue()


