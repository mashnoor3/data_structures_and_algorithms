"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    if root.left:
        inOrder(root.left)
    if root:
        # Python 2
        # print root.data,
        # Python 3:
        print (root.data, end= ' ')
    if root.right:
        inOrder(root.right)
