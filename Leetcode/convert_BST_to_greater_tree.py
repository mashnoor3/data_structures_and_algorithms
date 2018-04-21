'''
Problem Info:

Website:       Leetcode
Problem Name:  538. Convert BST to Greater Tree

Problem:
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus sum of all keys
greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

Solution:
Explained in-line with comments.

Time complexity:    O(n)
                    A binary tree has no cycles by definition,
                    so convertBST gets called on each node no more than once.
                    Other than the recursive calls, convertBST does a constant
                    amount of work, so a linear number of calls to convertBST
                    will run in linear time.

Space complexity:   O(n)
                    Using the prior assertion that convertBST is called a linear
                    number of times, we can also show that the entire algorithm
                    has linear space complexity. Consider the worst case, a tree
                    with only right (or only left) subtrees. The call stack will
                    grow until the end of the longest path is reached, which in
                    this case includes all nn nodes.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.currSum = 0

    def convertBST(self, root):
        # Basically just gotta do in order traversal in REVERSE
        # while updating the sum variable.
        # Recall for in order traveral it's left then right.
        # But want to visit bigger nodes first, therefore right them left,
        # therefore reverse in order traveral

        # Edge case: if the input is Null
        # AND base case
        if not root:
            return root

        if root.right:
            self.convertBST(root.right)
        self.currSum += root.val
        root.val = self.currSum

        if root.left:
            self.convertBST(root.left)

        return root

# ------------------------------------------------------------------------------

class Solution2:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convertBSTHelper(node, currSum):
            if not node:
                return currSum

            if node.right:
                currSum = convertBSTHelper(node.right, currSum)
            currSum += node.val
            node.val = currSum

            if node.left:
                currSum = convertBSTHelper(node.left, currSum)

            return currSum

        convertBSTHelper(root, 0)

        return root
