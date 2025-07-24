# Find the starting node of a loop in linked list
# ✔ Workflow: Floyd's cycle detection + find entry point

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLoopStart(head):
    if not head or not head.next:
        return None
    
    # Phase 1: Detect if loop exists using Floyd's algorithm
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # If no loop found
    if not fast or not fast.next:
        return None
    
    # Phase 2: Find the start of the loop
    # Reset slow to head, keep fast at meeting point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next  # Move both one step at a time
    
    return slow  # This is the start of the loop

# Real-world use: Finding entry point in routing loops.
# ✅ Output: Node data

# 👉 Example usage with print
# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (loop back to node 3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3  # Creating loop - points back to n3

start = findLoopStart(n1)
if start:
    print("Loop starts at node with data:", start.data)  # Output: 3
else:
    print("No loop")

# Test with no loop
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n6.next = n7
n7.next = n8

start_no_loop = findLoopStart(n6)
if start_no_loop:
    print("Loop starts at node with data:", start_no_loop.data)
else:
    print("No loop found")  # Output: No loop found

# 💡 **Explanation:**
# Phase 1: Use Floyd's algorithm to detect loop
# Phase 2: Reset slow to head; moving both pointers one step at a time 
# gives the loop start node due to mathematical properties of the cycle.