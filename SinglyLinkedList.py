"""Implement a singly linked list class with the following methods:
append(data): Adds a new node with the specified data at the end of the list.
prepend(data): Adds a new node with the specified data at the beginning of the list.
print_list(): Prints all the elements in the list."""

# Define Class Node
class Node:
    def __init__(self, data):
        # Store the value for the current node in data
        self.data = data
        # Manage the pointers or references or links
        self.next = None
class SingleLinkedList:
    def __init__(self):
        # the head will point to the first node in the list
        self.head = None

    def prepend(self, data):
        #create a new node to store the given value
        new_node = Node(data)
        # make the new node as the head of the linked list
        new_node.next = self.head
        # make the new node as the new head of the linked list
        self.head = new_node


    def append(self, data):
        # create a new node to store the given value
        new_node = Node(data)

        # If the list is empty make new node as the head
        if self.head is None:
            self.head = new_node
            return
        # Otherwise loop through the end of the list or traverse
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        # Start with head
        current = self.head

        while current:
            print(current.data)
            # move to the next value
            current = current.next

mylist = SingleLinkedList()

mylist.append(100)
mylist.append(150)

mylist.prepend(50)

mylist.print_list()




