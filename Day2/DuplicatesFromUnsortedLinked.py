#  Fact Points:
# Time Complexity: O(n) (जहाँ n = nodes की संख्या)

# Space Complexity: O(n) (एक set इस्तेमाल हो रहा है duplicates track करने के लिए)

# Input: Singly Linked List

# Output: Modified Linked List with unique values only

# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to remove duplicates from the linked list
def removeDuplicates(head):
    if not head:
        return None

    seen = set()        # To store unique node data
    curr = head         # Start from head
    prev = None         # Track previous node

    # Traverse the list
    while curr:
        if curr.data in seen:
            # Duplicate found, skip current node
            prev.next = curr.next
        else:
            # Not a duplicate, add to seen and move prev
            seen.add(curr.data)
            prev = curr
        curr = curr.next
    return head

# Helper function to print linked list
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example usage:
# Creating Linked List: 1 -> 2 -> 3 -> 2 -> 4 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(3)

print("Original List:")
printList(head)

head = removeDuplicates(head)

print("\nList after removing duplicates:")
printList(head)

# Original List:
# 1 -> 2 -> 3 -> 2 -> 4 -> 3 -> None

# List after removing duplicates:
# 1 -> 2 -> 3 -> 4 -> None
