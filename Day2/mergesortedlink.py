# 7. Merge two sorted linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLists(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

# Real-world use: Merging sorted streams in real-time processing.
# ✅ Output: Merged list

# 👉 Example usage with print
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

b = Node(2)
b.next = Node(4)
b.next.next = Node(6)

merged = mergeLists(a, b)
print("Merged list:", end=" ")
while merged:
    print(merged.data, end=" ")
    merged = merged.next
print()

# Merged list: 1 2 3 4 5 6 

# 💡 **Explanation:**
# Compare current nodes, append smaller, move pointer forward.

# 🌍 **Real-World Applications:**
# 1. Database query optimization - merging sorted result sets
# 2. External sorting algorithms - merging sorted chunks from disk
# 3. Real-time data processing - combining sorted sensor readings
# 4. Web search engines - merging sorted index results
# 5. Financial systems - combining sorted transaction logs
# 6. Video streaming - merging sorted timestamps from multiple sources
# 7. Operating systems - merging sorted process queues