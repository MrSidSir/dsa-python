# 8. Find intersection of two linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getIntersection(headA, headB):
    if not headA or not headB:
        return None
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA

# Real-world use: Detecting shared memory or resource allocation.
# ✅ Output: Node data

# 👉 Example usage with print
# Creating intersecting lists
c = Node(8)
c.next = Node(10)

x = Node(3)
x.next = Node(7)
x.next.next = c

y = Node(99)
y.next = c

intersection = getIntersection(x, y)
if intersection:
    print("Intersection at node with data:", intersection.data)
else:
    print("No intersection")

    # output:-Intersection at node with data: 8

# 💡 **Explanation:**
# Pointers switch heads when reaching end; syncs to meet at intersection.

# 🔍 **Algorithm Facts:**
# • Time Complexity: O(m + n) where m, n are list lengths
# • Space Complexity: O(1) - uses only two pointers
# • Works by equalizing traversal distances through path switching
# • If no intersection exists, both pointers become None simultaneously

# 🌍 **Real-World Applications:**
# 1. Memory Management - Detecting shared memory blocks between processes
# 2. Version Control Systems - Finding common ancestor commits (Git merge base)
# 3. Social Networks - Finding mutual connections between users
# 4. File Systems - Detecting hard links pointing to same inode
# 5. Network Topology - Finding shared network paths between nodes
# 6. Database Systems - Identifying shared foreign key relationships
# 7. Compiler Design - Detecting shared code paths in control flow graphs
# 8. Resource Allocation - Finding shared resources between threads