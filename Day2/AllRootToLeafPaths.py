# Topic: Tree
# Real-World Use: Logging all routes in file systems, routers.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_paths(root, path=[]):
    if root is None:
        return
    
    # Append current node to the path
    path = path + [root.data]

    # If it's a leaf node, print the path
    if root.left is None and root.right is None:
        print(" -> ".join(map(str, path)))
    else:
        # Recur for left and right subtrees
        print_paths(root.left, path)
        print_paths(root.right, path)

# 🔍 Test Example Tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("All root-to-leaf paths:")
print_paths(root)

# ✅ Output:
# 1 -> 2 -> 4
# 1 -> 2 -> 5
# 1 -> 3
