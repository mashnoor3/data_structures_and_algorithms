'''
Problem Info:

Website:       Leetcode
Problem Name:  669. Trim a Binary Search Tree

Problem:
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return
the new root of the trimmed binary search tree.

Solution:
Explained in-line with comments.

Time complexity:    O(n)
Space complexity:   O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None

        # If root is not within range, go down left or right.
        # If smaller than lower bound, go right
        if root.val < L:
            return self.trimBST(root.right, L, R)
        # If bigger than upper bound, go left
        if root.val > R:
            return self.trimBST(root.left, L, R)

        # Within range, so get correct left and right recursively
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root
