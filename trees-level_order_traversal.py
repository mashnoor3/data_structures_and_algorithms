"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def enqueue (alist, item):
    alist.insert(0, item)

def dequeue (alist):
    return alist.pop()

def levelOrder(root):
   queue = []
   enqueue(queue, root)

   while len(queue) > 0:
       currentNode = dequeue(queue)
       # Python 2
       # print currentNode.data,
       # Python 3
       print (currentNode.data, end=" ")

       if currentNode.left:
           enqueue(queue, currentNode.left)
       if currentNode.right:
           enqueue(queue, currentNode.right)
