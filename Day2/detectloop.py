# 3. Detect loop in linked list
# ✔ Workflow: Slow and fast pointers; if they meet, loop exists.

class Node:
    def __init__(self, data):  # Fixed: __init__ instead of _init_
        self.data = data
        self.next = None

def hasLoop(head):  # Fixed: function name and indentation
    if not head or not head.next:  # Handle edge cases
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True
    return False  # Fixed: moved outside the while loop

# Real-world use: Detecting cycles in network packets or dependency graphs.
# ✅ Output: True/False

# 👉 Example usage with print
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
n3.next = n1  # creating loop

print("Loop detected:", hasLoop(n1))  # Output: True

# Test without loop
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n4.next = n5
n5.next = n6
# n6.next is None (no loop)

print("Loop detected (no loop):", hasLoop(n4))  # Output: False

# 💡 **Explanation:**
# fast moves 2 steps, slow moves 1 step, if loop exists they meet.

# output:- Loop detected: True
# Loop detected (no loop): False
