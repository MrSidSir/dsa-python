# Define the ListNode class first
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        """Helper method to print the linked list"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

# Recursive function to reverse linked list
def reverseRec(head):
    # Base case: if head is None or next is None, return head
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    rest = reverseRec(head.next)
    
    # Adjust pointers
    head.next.next = head
    head.next = None
    
    return rest

# Test the function
if __name__ == "__main__":
    print("Creating linked list: 1 -> 2 -> 3 -> 4 -> 5")
    
    # Create test linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    print("Original list:", head)
    
    # Reverse the linked list
    reversed_head = reverseRec(head)
    
    print("Reversed list:", reversed_head)
    print("✅ Linked list reversed successfully!")

#     Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
# Original list: 1 -> 2 -> 3 -> 4 -> 5
# Reversed list: 5 -> 4 -> 3 -> 2 -> 1
# ✅ Linked list reversed successfully!