# Problem:
# Complete the preOrder function in your editor below, which has  parameter:
# a pointer to the root of a binary tree. It must print the values in the tree's
# preorder traversal as a single line of space-separated values.


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def preOrder(root):
    if root:
        # Python 2:
        # print root.data,
        # Python 3:
        print (root.data, end= ' ')
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
