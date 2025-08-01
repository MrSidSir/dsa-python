# Real-World Use:
# यह function यह चेक करता है कि एक singly linked list palindrome है या नहीं (जैसे: 1→2→2→1)

# Useful in: text processors, string comparison engines, DNA sequence analysis, etc.
# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to check if linked list is a palindrome
def isPalindrome(head):
    vals = []
    
    # Step 1: Traverse the list and store values
    while head:
        vals.append(head.data)
        head = head.next

    # Step 2: Check if list is same as its reverse
    return vals == vals[::-1]

# Helper function to print linked list
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
# Creating Linked List: 1 -> 2 -> 2 -> 1 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print("Original List:")
printList(head)

# Check if it's a palindrome
if isPalindrome(head):
    print("✅ The linked list is a palindrome.")
else:
    print("❌ The linked list is NOT a palindrome.")

# Original List:
# 1 -> 2 -> 2 -> 1 -> None
# ✅ The linked list is a palindrome.