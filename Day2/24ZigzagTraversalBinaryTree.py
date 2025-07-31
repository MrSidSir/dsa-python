# Topic: Tree
# Real-World Use: Graphical tree rendering or UI frameworks.
def zigzag(root):
    if not root:  return []
    result,  queue, left = [], [root], True
    while queue:
        level, size = [], len(queue)
        for _ in range(size):
            node = queue.pop(0)
            level.append(node.data)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            result.append(level if left else leel[:: -1])
            left = not left
            return result
