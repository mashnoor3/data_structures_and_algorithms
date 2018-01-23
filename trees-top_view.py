"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

import collections

def enqueue (alist, item):
    alist.insert(0, item)

def dequeue (alist):
    return alist.pop()

def topView(root):
    # Hashtable values are Lists of the nodes, and key is horizontal distance (Hd)
    # away from the root. Root has Hd = 0
    hashTable = collections.defaultdict(list)
    queue = []

    enqueue(queue, root)
    hashTable[0].append(root)

    while len(queue) > 0:
        currentNode = dequeue(queue)

        if currentNode.left:
            enqueue(queue, currentNode.left)
            # add it to the hashTable with corrent HD

        if currentNode.right:
            enqueue(queue, currentNode.right)
            # add it to the hashTable with corrent HD
