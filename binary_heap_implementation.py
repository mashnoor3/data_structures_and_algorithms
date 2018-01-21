'''
Priority queue using a binary tree.

Need to maintain structure and order of the tree when doing insert and delete
operations.

Recall that for priority queue, the smallest element must be the root of the tree.
Keep the tree balanced by using a complete binary tree, with the exception of the
bottom level. Which will be filled from left to right.

Since complete binary tree, can represent using a list (no need for nodes and references)
approach. Parent at position p will have left child at 2p, and right child at 2p.

'''

class BinaryHeap(object):
    # Want to do integer division to access the parent of a node.
    # Therefore need to use a placeholder for location
    def __init__(self):
        self.currentSize = 0
        self.heapList = [0]

    # Append to the end of the list, and percolate up.
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    # Helper function for insert()
    def percUp(self, clocation):
        # Keep going up as long as the current node has a parent
        while clocation // 2 > 0:
            # If larger than parent, then swap
            if self.heapList[clocation] > self.heapList[clocation // 2]:
                self.heapList[clocation], self.heapList[clocation // 2] = self.heapList[clocation // 2], self.heapList[clocation]
            # Update clocation
            clocation = clocation // 2

    # Remove the root of the tree, and put last element at the root to
    # maintain strcuture. Then call helper function percDown to restore order.
    def delMin(self):
        minvalue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)
        return minvalue

    # Helper function for delMin
    def percDown(self, clocation):
        # Keep going down as long as not the last node
        while clocation * 2 <= self.currentSize:
            # Find the index location of the min child of the current node. Then check to swap
            mc = self.findMinChild(clocation)
            if self.heapList[clocation] > self.heapList[mc]:
                self.heapList[clocation], self.heapList[mc] = self.heapList[mc], self.heapList[clocation]
            # Update location
            clocation = clocation * 2

    # Helper function for percDown
    def findMinChild(self, clocation):
        # First case is that there is only one child (by the way I defined it, only left child)
        if (clocation*2 + 1) > self.currentSize:
            return clocation*2
        else:
            if self.heapList[clocation*2] < self.heapList[clocation*2 +1]:
                return clocation*2
            else:
                return clocation*2 + 1

    def findMin(self):
        return self.heapList[1]

    # Given a list (random list that does not have structure of a bin heap)
    # Create a bin heap
    def buildHeap(self, aList):
        # Size of the heap will be t
        self.currentSize = len(aList)
        # Need to add the dummy index location
        self.heapList = [0] + aList[:]
        # Start at the middle (since bottom half are leaf nodes)
        i = len(aList) // 2

        # Starting at the half point, iterate through all the nodes and restore order
        while i > 0:
            self.percDown(i)
            i = i - 1

################################################################################
################################## TEST CASES ##################################
################################################################################
m = BinaryHeap()
m.heapList = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
m.currentSize = 10
print(m.heapList)
print(m.delMin())
print(m.heapList)

bh = BinaryHeap()
bh.buildHeap([9,5,6,2,3])
print(bh.heapList)
