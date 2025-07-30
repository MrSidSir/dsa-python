# Topic: Tree
# Real-World Use: Tracing file paths, directory trees, organizational hierarchies

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_ancestors(root, target):
    if not root:
        return False

    if root.data == target:
        return True

    # Check if target is present in left or right subtree
    if print_ancestors(root.left, target) or print_ancestors(root.right, target):
        print(root.data)  # If yes, this node is an ancestor
        return True

    return False

# 🔍 Test Example Tree
#         1
#        / \
#       2   3
#      / \
#     4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Ancestors of 5:")
print_ancestors(root, 5)
# ✅ Output: 
# 2
# 1
