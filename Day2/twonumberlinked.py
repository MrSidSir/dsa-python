# 6. Add two numbers represented by linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addLists(l1, l2):
    """Add two numbers represented as linked lists"""
    dummy = Node(0)  # Fixed: Initialize dummy node
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        s = (l1.data if l1 else 0) + (l2.data if l2 else 0) + carry
        carry, val = divmod(s, 10)
        curr.next = Node(val)
        curr = curr.next 
        
        if l1: 
            l1 = l1.next 
        if l2: 
            l2 = l2.next 
    
    return dummy.next

def printList(head):
    """Print linked list in a readable format"""
    result = []
    current = head
    while current:
        result.append(str(current.data))
        current = current.next
    return " -> ".join(result)

def printNumber(head):
    """Print the number represented by linked list (digits in reverse)"""
    digits = []
    current = head
    while current:
        digits.append(str(current.data))
        current = current.next
    return "".join(reversed(digits))

# Real-world use: Large integer addition in financial software.
# ✅ Output: Sum list

# 👉 Example usage with print
print("=== Adding Two Numbers Using Linked Lists ===")

# Number1: 342 represented as (2->4->3) [least significant digit first]
print("Creating first number: 342")
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
print("L1 structure:", printList(l1))
print("L1 represents number:", printNumber(l1))

# Number2: 465 represented as (5->6->4) 
print("\nCreating second number: 465")
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)
print("L2 structure:", printList(l2))
print("L2 represents number:", printNumber(l2))

# Add the numbers
print("\n=== Addition Process ===")
print("342 + 465 = 807")
res = addLists(l1, l2)

print("\nResult structure:", printList(res))
print("Result represents number:", printNumber(res))

# Print digit by digit (corrected logic)
print("\nSum list digits:", end=" ")
current = res
while current:
    print(current.data, end=" ")
    current = current.next
print()

print("\n=== Another Example ===")
# Example 2: 999 + 1 = 1000
print("Adding 999 + 1:")

# 999 as (9->9->9)
num1 = Node(9)
num1.next = Node(9)
num1.next.next = Node(9)

# 1 as (1)
num2 = Node(1)

result = addLists(num1, num2)
print("999 + 1 =", printNumber(result))
print("Result structure:", printList(result))

print("\n=== Edge Case: Different Lengths ===")
# Example 3: 50 + 123 = 173
print("Adding 50 + 123:")

# 50 as (0->5)
a = Node(0)
a.next = Node(5)

# 123 as (3->2->1)
b = Node(3)
b.next = Node(2)
b.next.next = Node(1)

result2 = addLists(a, b)
print("50 + 123 =", printNumber(result2))
print("Result structure:", printList(result2))


# === Adding Two Numbers Using Linked Lists ===
# Creating first number: 342
# L1 structure: 2 -> 4 -> 3
# L1 represents number: 342

# Creating second number: 465
# L2 structure: 5 -> 6 -> 4
# L2 represents number: 465

# === Addition Process ===
# 342 + 465 = 807

# Result structure: 7 -> 0 -> 8
# Result represents number: 807

# Sum list digits: 7 0 8 

# === Another Example ===
# Adding 999 + 1:
# 999 + 1 = 1000
# Result structure: 0 -> 0 -> 0 -> 1

# === Edge Case: Different Lengths ===
# Adding 50 + 123:
# 50 + 123 = 173
# Result structure: 3 -> 7 -> 1


# 💡 **Explanation:**
# 1. Numbers are stored in reverse order (least significant digit first)
# 2. Traverse both lists simultaneously, adding digits with carry
# 3. Use divmod() to get carry and current digit
# 4. Create new nodes for result digits
# 5. Continue until both lists are exhausted and no carry remains