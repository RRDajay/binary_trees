def preorderTraversal(node, traversal):
    if node:
        traversal += (str(node.value) + "-")
        traversal = preorderTraversal(node.left, traversal)
        traversal = preorderTraversal(node.right, traversal)

    return traversal

def inorderTraversal(node, traversal):

    if node:
        traversal = inorderTraversal(node.left, traversal)
        traversal += (str(node.value) + "-")
        traversal = inorderTraversal(node.right, traversal)

    return traversal

def postorderTraversal(node, traversal):

    if node:
        traversal = postorderTraversal(node.left, traversal)
        traversal = postorderTraversal(node.right, traversal)
        traversal += (str(node.value) + "-")

    return traversal
