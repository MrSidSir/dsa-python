# Complete solution: Detect, Find Start, and Remove Loop from Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hasLoop(head):
    """Detect if loop exists using Floyd's algorithm"""
    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True
    return False

def findLoopStart(head):
    """Find the starting node of the loop"""
    if not head or not head.next:
        return None
    
    # Phase 1: Detect if loop exists
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
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

def removeLoop(head):
    """Remove loop from linked list"""
    loop_node = findLoopStart(head)
    if not loop_node:
        return  # No loop to remove
    
    # Find the node just before the loop start
    ptr = loop_node
    while ptr.next != loop_node:
        ptr = ptr.next
    
    # Break the loop
    ptr.next = None

def printList(head, max_nodes=10):
    """Print linked list (with safety limit to avoid infinite loop)"""
    current = head
    count = 0
    result = []
    
    while current and count < max_nodes:
        result.append(str(current.data))
        current = current.next
        count += 1
    
    if current:  # If we stopped due to limit
        result.append("... (truncated)")
    
    print(" -> ".join(result))

# Real-world use: Fixing corrupted linked list data structures.
# ✅ Output: Updated list

# 👉 Example usage with print
print("=== Creating Linked List with Loop ===")

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
n5.next = n3  # Creating loop

print("Original list structure: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (loop)")
print("Loop detected:", hasLoop(n1))  # Output: True

# Find loop start
start = findLoopStart(n1)
if start:
    print("Loop starts at node with data:", start.data)  # Output: 3

print("\n=== Removing Loop ===")
removeLoop(n1)

print("After removing loop:")
print("Loop exists now:", hasLoop(n1))  # Output: False
print("List after loop removal:")
printList(n1)  # Output: 1 -> 2 -> 3 -> 4 -> 5

print("\n=== Testing with No Loop ===")
# Test with a list that has no loop
n6 = Node(10)
n7 = Node(20)
n8 = Node(30)
n6.next = n7
n7.next = n8

print("List without loop:")
printList(n6)
print("Loop detected:", hasLoop(n6))  # Output: False
removeLoop(n6)  # Should do nothing
print("After removeLoop call (no change expected):")
printList(n6)

# === Creating Linked List with Loop ===
# Original list structure: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (loop)
# Loop detected: True
# Loop starts at node with data: 3

# === Removing Loop ===
# After removing loop:
# Loop exists now: False
# List after loop removal:
# 1 -> 2 -> 3 -> 4 -> 5

# === Testing with No Loop ===
# List without loop:
# 10 -> 20 -> 30
# Loop detected: False
# After removeLoop call (no change expected):
# 10 -> 20 -> 30

# 💡 **Explanation:**
# 1. findLoopStart() finds the first node of the loop
# 2. Traverse from loop start until we find the node that points back to loop start
# 3. Set that node's next to None, breaking the loop