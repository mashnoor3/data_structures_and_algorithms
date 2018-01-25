'''
Question Info
HackerRank
Tree: Binary Search Tree Find LCA
'''

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def lca(root , v1 , v2):
    if v1 > root.data and v2 > root.data:
        lca(root.right, v1, v2)
    elif v1 < root.data and v2 < root.data:
        lca(root.left, v1, v2)
    else:
        return root
