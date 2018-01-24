'''
Question Info
HackerRank
Tree: Top View
'''

# Method 1: Solve iteratively. Use a queue and a hashtable

import collections

def enqueue (alist, item):
    alist.insert(0, item)

def dequeue (alist):
    return alist.pop()

def topView(root):
    # Hashtable values are Lists of the nodes, and key is horizontal distance (Hd)
    # away from the root. Root has Hd = 0
    hashTable = collections.defaultdict(list)
    # Each element in the queue is a pair. [Node, Hd]
    queue = []

    enqueue(queue, [root, 0])
    hashTable[0].append(root)

    while len(queue) > 0:
        current = dequeue(queue)

        if current[0].left:
            # Enque the part: the left child node, and updated Hd
            enqueue(queue, [current[0].left, current[1]-1 ])
            # Using add the left child node to the hashtable, using the calculated Hd
            hashTable[current[1]-1].append(current[0].left)

        if current[0].right:
            # Enque the part: the right child node, and updated Hd
            enqueue(queue, [current[0].right, current[1]+1])
            # Using add the right child node to the hashtable, using the calculated Hd
            hashTable[current[1]+1].append(current[0].right)

    # Print the first item of the list for each entry in the Hashtable
    for key in hashTable:
        print (hashTable[key][0].data)



# Method 2: Solve recursively. Traverse all the way left and print upwards to root
# then traverse right and print along the way

def goLeft(node):
    # For left, need to traverse first then print
    if node.left:
        goLeft(node.left)
    # Python 2
    # print node.data,
    # Python 3
    print (node.data, end=" ")

def goRight(node):
    # For right, need to print as traversing down
    # Python 2
    # print node.data,
    # Python 3
    print (node.data, end=" ")

    if node.right:
        goRight(node.right)

def topView(root):
    if root.left:
        goLeft(root.left)

    # Python 2
    # print root.data,
    # Python 3
    print (root.data, end=" ")

    if root.right:
        goRight(root.right)
