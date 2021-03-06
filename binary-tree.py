from treetraversal import preorderTraversal, postorderTraversal, inorderTraversal

class Node(object):

    def __init__(self,value):
        self.value =  value
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

#      1
#     /   \
#    2     3
#   / \   / \
#  4  5  6   7

# Set-up Binary Tree

if __name__ == "__main__":
    
    tree = BinaryTree(1)
    
    tree.root.left = Node(2)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right = Node(3)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print('preorder traversal', preorderTraversal(tree.root, ''))
    print('inorder traversal', inorderTraversal(tree.root, ''))
    print('postorder traversal', postorderTraversal(tree.root, ''))

