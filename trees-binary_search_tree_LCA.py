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
    # Both are in the right subtree
    if v1 > root.data and v2 > root.data:
        lca(root.right, v1, v2)
    # Both are in the left subtree
    elif v1 < root.data and v2 < root.data:
        lca(root.left, v1, v2)
    else:
        # A node can be descendent of itself. So if v2 is a child of v1,
        # then return v1
        return root
