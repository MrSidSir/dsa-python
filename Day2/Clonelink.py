class RandNode:
    def __init__(self, data):  # Fixed: __init__ (double underscores)
        self.data = data
        self.next = None
        self.random = None

def cloneList(head):
    if not head:
        return None
    
    # Step 1: Insert cloned nodes adjacent to originals
    curr = head
    while curr:
        newNode = RandNode(curr.data)
        newNode.next = curr.next  # Fixed: should point to curr.next, not newNode
        curr.next = newNode
        curr = newNode.next
    
    # Step 2: Assign random pointers to cloned nodes
    curr = head
    while curr:
        if curr.random:  # Fixed: check curr.random first
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    # Step 3: Separate the cloned list
    curr = head
    cloneHead = head.next
    while curr:
        temp = curr.next
        curr.next = temp.next
        if temp.next:  # Fixed: check if temp.next exists
            temp.next = temp.next.next
        curr = curr.next
    
    return cloneHead

# Example usage
n1 = RandNode(1)
n2 = RandNode(2)
n1.next = n2
n1.random = n2  # Fixed: removed duplicate line
n2.random = n2

clone = cloneList(n1)
print("Original node data:", n1.data, "random:", n1.random.data)
print("Cloned node data:", clone.data, "random:", clone.random.data)

# output: Original node data: 1 random: 2
# Cloned node data: 1 random: 2