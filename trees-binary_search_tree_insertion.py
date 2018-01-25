'''
Question Info
HackerRank
Tree: Binary Search Tree Insertion
'''


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""


def insert(root,val):
    if not root:
        root = Node(val)
    else:
        if val > root.data:
            if root.right:
                insert(root.right, val)
            else:
                root.right = Node(val)
        else:
            if root.left:
                insert(root.left, val)
            else:
                root.left = Node(val)

    return root
