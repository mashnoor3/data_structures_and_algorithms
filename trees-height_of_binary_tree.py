'''
Problem:
The height of a binary tree is the number of edges between the tree's root and
its furthest leaf. This means that a tree containing a single node has a
height of 0.

Complete the getHeight function provided in your editor so that it returns the
height of a binary tree. This function has a parameter, root, which is a pointer
to the root node of a binary tree

Note -The Height of binary tree with single node is taken as zero.
'''

'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    # Base case:
    # This has to be -1 and not 0
    # Consider just a single node tree, if base case returns 0, then the height would've been 1
    # But problem statement states height of single node tree is 0
    if  root == None:
        return -1
    # Rerursive case:
    else:
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        return max(leftHeight, rightHeight) + 1
