# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.out = []

    # Recursive Sol
    def inorderTraversal1(self, root):
        if not root:
            return self.out

        if root.left:
            self.inorderTraversal(root.left)

        self.out.append(root.val)

        if root.right:
            self.inorderTraversal(root.right)

        return self.out

    def inorderTraversal(self, root):
        pass

    # Iterative solution
    def inorderTraversal(self, root):
        stack, output = [], []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                output.append(tmp.val)
                root = tmp.right
        return output


stack = [1,2]
print(stack)
print(len(stack))
stack.pop()
stack.pop()
print(len(stack))
