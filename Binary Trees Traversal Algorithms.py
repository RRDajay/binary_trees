class Node(object):

    def __init__(self,value):
        self.value =  value
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def _preorder_traversal(self, node, traversal):
        if node:
            traversal += (str(node.value) + "-")
            traversal = self._preorder_traversal(node.left, traversal)
            traversal = self._preorder_traversal(node.right, traversal)

        print(self.sum)
        return traversal

    def _inorder_traversal(self, node, traversal):

        if node:
            traversal = self._inorder_traversal(node.left, traversal)
            traversal += (str(node.value) + "-")
            traversal = self._inorder_traversal(node.right, traversal)

        return traversal

    def _postorder_traversal(self, node, traversal):

        if node:
            traversal = self._postorder_traversal(node.left, traversal)
            traversal = self._postorder_traversal(node.right, traversal)
            traversal += (str(node.value) + "-")

        return traversal




#       1
#     /   \
#    2     3
#   / \   / \
#  4  5  6   7

# Set-up Binary Tree
tree = BinaryTree()
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#Binary Tree Traversals
#Pre Order Traversal

print('preorder traversal', tree._preorder_traversal(tree.root, ''))
print('inorder traversal', tree._inorder_traversal(tree.root, ''))
print('postorder traversal', tree._postorder_traversal(tree.root, ''))

