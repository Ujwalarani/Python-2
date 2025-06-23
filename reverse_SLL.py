"""Problem: Reverse a Singly Linked List using Recursion - Choose your own list and reverse it recursively """

# Create Linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 #Create a function to recursively reverse SLL
def reverse_linkedlist(head):
    #check if the list is empty, or it has one node
    if head is None or head.next is None:
        return head
    # Recursively call the function to get th rest of the list
    new_head = reverse_linkedlist(head.next)

    # reverse the linked direction
    head.next.next = head
    head.next = None

    return new_head    # this will return the new head of the reversed list

def print_list(node):
    while node:
        print(node.value, end="-->")
        node = node.next
    print("None")

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print("This is the original List: ")
    print_list(head)

    reversed_head = reverse_linkedlist(head)

    print("Reversed List: ")
    print_list(reversed_head)


