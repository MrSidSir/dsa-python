# Topic: Tree
# Real-World Use: Rebuilding directory or DOM trees from saved orders

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    # ✅ Base case: if either list is empty, return None
    if not preorder or not inorder:
        return None

    # ✅ The first element in preorder is always the root
    root_val = preorder[0]
    root = Node(root_val)

    # ✅ Find the index of root in inorder traversal
    idx = inorder.index(root_val)

    # ✅ Build left subtree using:
    # preorder[1 : idx+1] → left subtree elements in preorder
    # inorder[:idx]      → left subtree elements in inorder
    root.left = buildTree(preorder[1:idx+1], inorder[:idx])

    # ✅ Build right subtree using:
    # preorder[idx+1:]   → right subtree in preorder
    # inorder[idx+1:]    → right subtree in inorder
    root.right = buildTree(preorder[idx+1:], inorder[idx+1:])

    return root

# 🔁 Helper to Print Tree in Inorder (for verification)
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=' ')
        printInorder(root.right)

# 🔍 Test Example
pre = [3, 9, 20, 15, 7]
ino = [9, 3, 15, 20, 7]

tree = buildTree(pre, ino)

print("Inorder traversal of rebuilt tree:")
printInorder(tree)  # ✅ Output should be: 9 3 15 20 7
# output:-Inorder traversal of rebuilt tree:
# 9 3 15 20 7
