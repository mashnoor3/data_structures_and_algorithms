"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    if root:
        # Python 2
        # print root.data,
        # Python 3:
        print (root.data, end= ' ')
