# ✅ Node definition for singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ✅ Function to remove N-th node from end of list
def removeNthFromEnd(head, n):
    """
    Removes the n-th node from the end of a singly linked list using two pointers.

    👉 Real-World Use:
        - Removing last N-th watched video, N-th transaction from end, etc.
        - Used in system design for data cleanup or memory buffering.
    👉 Fact:
        - Time Complexity: O(L), where L is the length of the linked list
        - Space Complexity: O(1), uses constant space
    """

    # 📍 Step 1: Add a dummy node to handle edge cases smoothly (like deleting the head)
    dummy = ListNode(0)
    dummy.next = head

    # 📍 Step 2: Initialize both fast and slow pointers at dummy
    fast = slow = dummy

    # 📍 Step 3: Move fast pointer 'n' steps ahead
    for _ in range(n):
        fast = fast.next

    # 📍 Step 4: Move both fast and slow until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # 📍 Step 5: Delete the N-th node from end
    slow.next = slow.next.next

    # 📍 Step 6: Return the head of the modified list
    return dummy.next

# ✅ Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# ✅ Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")

# ✅ Example Test Case
if __name__ == "__main__":
    # Input linked list: [1, 2, 3, 4, 5]
    head = create_linked_list([1, 2, 3, 4, 5])
    n = 2

    print("🔹 Original List:")
    print_linked_list(head)

    # Remove the 2nd node from the end (Expected list: [1, 2, 3, 5])
    updated_head = removeNthFromEnd(head, n)

    print(f"\n🔹 After Removing {n}th Node from End:")
    print_linked_list(updated_head)

# output:🔹 Original List:
# 1 → 2 → 3 → 4 → 5 → None

# 🔹 After Removing 2th Node from End:
# 1 → 2 → 3 → 5 → None