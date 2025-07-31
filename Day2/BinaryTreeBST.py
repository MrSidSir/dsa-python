# Topic: Tree
# Real-World Use: Data integrity in hierarchical DBs (e.g., LDAP, file systems, XML)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root, min_val=float("-inf"), max_val=float("inf")):
    # ✅ Base case: An empty tree is a valid BST
    if not root:
        return True

    # ✅ Check if current node breaks the BST property
    if not (min_val < root.data < max_val):
        return False

    # ✅ Recur for left subtree:
    # All values must be < current node's value
    is_left_bst = isBST(root.left, min_val, root.data)

    # ✅ Recur for right subtree:
    # All values must be > current node's value
    is_right_bst = isBST(root.right, root.data, max_val)

    # ✅ Tree is BST only if both left and right subtrees are valid
    return is_left_bst and is_right_bst


# 🔍 Test Example

#        10
#       /  \
#      5   15
#         /  \
#        12   20

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)

print("Is this a valid BST?", isBST(root))  # ✅ Output: True
