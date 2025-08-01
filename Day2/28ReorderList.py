class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return

    # 🟩 Step 1: Find middle using slow and fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Now `slow` is at the middle node

    # 🟩 Step 2: Reverse the second half of the list
    prev, curr = None, slow.next
    slow.next = None  # Cut the list into two halves
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # Now `prev` is the head of the reversed second half

    # 🟩 Step 3: Merge both halves alternately
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

# 🔁 Helper function to create linked list from list
def createLinkedList(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# 🔍 Helper function to print linked list
def printLinkedList(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

# ✅ Example Use
head = createLinkedList([1, 2, 3, 4, 5])
print("Original List:")
printLinkedList(head)

reorderList(head)

# print("\nReordered List (Zigzag Style):")
# printLinkedList(head)

# Original List:
# 1 -> 2 -> 3 -> 4 -> 5

# Reordered List (Zigzag Style):
# 1 -> 5 -> 2 -> 4 -> 3

# Real-World Use:
# Used in displaying UI cards in zigzag or alternating patterns.


