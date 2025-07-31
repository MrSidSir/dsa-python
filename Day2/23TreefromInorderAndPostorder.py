# 🌐 Real-World Use: Rebuilding directory structures, DOM trees in browsers from saved traversal orders (like postorder/inorder)
# 📌 Fact: Postorder defines the root at the end, inorder defines left-root-right order.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def buildTree(postorder, inorder):
    if not postorder or not inorder:
        return None

    # ✅ Step 1: Last element in postorder is root
    root_val = postorder[-1]
    root = Node(root_val)

    # ✅ Step 2: Find index of root in inorder
    idx = inorder.index(root_val)

    # ✅ Step 3: Recursively build left and right subtrees
    root.left = buildTree(postorder[:idx], inorder[:idx])
    root.right = buildTree(postorder[idx:-1], inorder[idx+1:])

    return root

# ✅ Test: Tree from inorder and postorder
def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right)

# Example input
postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]

# Build tree and test
tree_root = buildTree(postorder, inorder)
print("Inorder traversal of reconstructed tree:", inorderTraversal(tree_root))
# output:-Inorder traversal of reconstructed tree: [9, 3, 15, 20, 7]