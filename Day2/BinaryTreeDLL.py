# Topic: Tree
# Real-World Use: Flattening hierarchical structures (like XML/HTML trees)

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def bTDLL(root):
    def convert(node):
        nonlocal last, head
        if not node:
            return
        
        # Recursively convert left subtree
        convert(node.left)

        # Link current node with last node in DLL
        if last:
            last.right = node
            node.left = last
        else:
            head = node  # First node becomes head

        last = node  # Update last processed node

        # Recursively convert right subtree
        convert(node.right)

    # Initialize pointers
    last, head = None, None
    convert(root)
    return head

# 🔁 Helper to Print Doubly Linked List
def printDLL(head):
    while head:
        print(head.data, end=" <-> " if head.right else "")
        head = head.right

# 🔍 Test Example
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

dll_head = bTDLL(root)
printDLL(dll_head)
# ✅ Output: 3 <-> 5 <-> 7 <-> 10 <-> 20
