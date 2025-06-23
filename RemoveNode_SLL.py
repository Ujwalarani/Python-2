"""Removing a Node from a Singly Linked List
====================================
Task: Implement a method remove(data) in the LinkedList class that removes the
first occurrence of a node with the specified data from the list."""


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
    # Method to remove the first node from the linked list
    def remove_first_node(self):
        if self.head is None:
            print("Nothing in the list to remove")
            return
        self.head = self.head.next
    # to find the number of nodes in a linked list
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


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

print("\nBefore removing the first item from the list:")
mylist.print_list()

# To Remove all nodes one by one
while mylist.head is not None:
    mylist.remove_first_node()
    print("After removal:")
    mylist.print_list()  # Optional, to visualize the process

print("List is now empty!")


print("After removing all items from the list:")
print(mylist.size())
mylist.print_list()



