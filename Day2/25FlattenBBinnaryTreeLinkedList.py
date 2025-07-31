# Topic: Tree - Flatten Binary Tree to Linked List
# Real-World Use: Serialize hierarchical data (e.g., tree, XML) into flat format for storage or transfer.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ✅ Function to flatten the tree
def flatten(root):
    if not root:
        return
    
    # 🔁 Recursively flatten left and right subtrees
    flatten(root.left)
    flatten(root.right)

    if root.left:
        # 🔄 Store original right subtree
        temp = root.right

        # 📌 Move left subtree to right
        root.right = root.left
        root.left = None  # ✅ Nullify left pointer

        # 🔍 Find tail of the new right subtree
        tail = root.right
        while tail.right:
            tail = tail.right
        
        # 🔗 Attach original right subtree
        tail.right = temp

# ✅ Helper: Print flattened tree
def print_flattened(root):
    while root:
        print(root.val, end=" → ")
        root = root.right
    print("None")

# ✅ Example Tree:
#         1
#        / \
#       2   5
#      / \   \
#     3   4   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

flatten(root)
print("Flattened tree (right-skewed):")
print_flattened(root)

# output:Flattened tree (right-skewed):
# 1 → 2 → 3 → 4 → 5 → 6 → None
# Real-World Use
# Serialize XML/HTML/JSON DOM Trees: Flatten for storage in databases or text-based formats.

# Tree → Linked List: Used in compilers, interpreters, file system backups, and UI virtual DOM flattening.