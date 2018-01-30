'''
Problem Info:

Website:       Leetcode
Problem Name:  617. Merge Two Binary Trees

Problem:
Given two binary trees and imagine that when you put one of them to cover the
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Solution:
Idea:               Do preorder traversal to traverse down both trees. At each
                    traversal check if current node isn't null, then add. Use
                    tree 1 as the updated tree to be returned. Then call
                    mergeTrees() with the left child, then right child.
                    If either of the children is null, then call the return the
                    other the child of the other tree. This will be added as
                    a subtree.

Time complexity:    O(n) (need to go through all nodes)
Space complexity:   O(logn) for average case, and O(n) for worst case (skewed tree)
'''

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1
