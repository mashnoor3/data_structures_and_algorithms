'''
2 Classes
BinarySearchTree: has a reference to the tree node that is the root of the tree
TreeNode: contains info for a node in the tree, like key, value, left child, right
child, parent
'''

class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    # Modifying the iter function to iterare from the root node
    def __iter__(self):
        return self.root.__iter__()

    '''
    Put method:
    First check if tree already has a root node, if not then insert as root node.
    Otherwise call the helper function _put.
    _put is a recursive function, keep going down the tree until find right location
    to put the node
    '''
    def put(self, key, val):
        # If root exists, need to call _put
        if self.root:
            self._put(key, val, self.root)
        # no root create this key/val pair as the root node
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            # Base case for when no leftchild and want to insert as left child
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            # Base case for when no rightchild and want to insert as right child
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    # In order to put items on the tree in similar syntax as the python dictionary
    # override the __setitem__ method
    def __setitem__(self,k,v):
        self.put(k,v)

    '''
    Get method:
    Similar to put, recursively search the tree until find the correct key
    '''
    def get(self, key):
        if self.root:
            node = self._get(self, key, self.root)
            if node:
                return node.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if currentNode:
            if currentNode.key == key:
                return currentNode
            else:
                if currentNode.key < key:
                    return self._get(key, currentNode.leftChild)
                else:
                    return self._get(key, currentNode.rightChild)
        else:
            return None

    # Override the __getitem__ method to be able to access value with a key similar to
    # a dictionary
    def __getitem__(self, key):
        return self.get(key)

    # Overriding the conatin method
    def __contain__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        # Case 1: tree more than 1 mode
        if self.size > 1:
            # first find the node that is to be removed
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError ('Key does not exist in tree')

        # Case 2: tree just 1 ndoe
        elif self.size == 1 and self.root.key == key:
                self.root = None
                self.size = self.size - 1

        # Case 3: key does not exist in tree
        else:
            raise KeyError ('Key does not exist in tree')

    # Succesor is the node that has the next largest key in the tree
    def findSuccessor(self):
        # Has a right child, then successor is the min
        if self.hasRightChild():
            succ = self.rightChild.findMinChild()
        else:
            # If is the left child, then successor is the parent
            if self.parent.leftChild == self:
                succ = self.parent
            # If is the right child, then successor is the successor of the parent
            # (excluding itself)
            else:
                # Can't include itself in the search
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                # Add itself bank in after search is complete
                self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    ''' For splice need to consider 3 cases:
        1. Has no childen (ie leaf node)
        2. Has only left child
        3. Has only right child
    '''
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                   self.parent.leftChild = None
            else:
                   self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                   if self.isLeftChild():
                      self.parent.leftChild = self.leftChild
                   else:
                      self.parent.rightChild = self.leftChild
                   self.leftChild.parent = self.parent
            else:
                   if self.isLeftChild():
                      self.parent.leftChild = self.rightChild
                   else:
                      self.parent.rightChild = self.rightChild
                   self.rightChild.parent = self.parent


    '''Three cases to consider once the node to be removed is found:
    1. Node has no children
    2. Node has both chilren
    3. Node has one child '''
    def remove(self, currentNode):
        #  1. Node has no children
        if currentNode.isLeaf():
            # It is the left child of its parent
            if currentNode.parent.leftChild == self:
                currentNode.parent.leftChild = None
            # It is the right child of its parent
            else:
                currentNode.parent.rightChild = None

        #  2. Node has both chilren
        # When the node has both children, don't know who to promote. Therefore need to
        # find a successor. The successor has to preserve the BST quality for both left
        # and right subtrees.
        # The successor can have at max 1 child.
        # Use helper function findSuccessor to find successor. spliceOut to
        # remove from original location, and inplace of the node to be removed.
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        #  3. Node has one child
        else:
            # 6 cases to consider:
            #     a. Has left child only
            #         1) Current node is a left child.
            #             - Update currentNode's leftChild's parent reference to the parent of the currentNode
            #             - Update currentNode's parent's leftChild reference to currentNode's leftChild
            #         2) Current node is a right child.
            #             - Update currentNode's rightChild's parent reference to the parent of the currentNode
            #             - Update currentNode's parent's rightChild reference to currentNode's leftChild
            #         to point to currentNode's leftChild
            #         3) Current node has no parent => currentNode is the isRoot
            #             - Replace key, payload, lc, rc of the root by calling replaceNodeData
            #
            #     b. Has right child only
            #         4. Symmetrical except for rightChild
            #         5. Symmetrical except for rightChild
            #         6. Symmetrical except for rightChild

            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

class TreeNode(object):
    def init(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild():
        return self.leftChild

    def hasRightChild():
        return self.rightChild

    def isLeftChild():
        return self.parent.leftChild == self

    def isRightChild():
        return self.parent.rightChild == self

    def isRoot():
        return not self.parent

    def isLeaf():
        # if has left child OR right child return false, otherwise return true
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren():
        return self.leftChild or self.rightChild

    def hasBothChildren():
        return self.leftChild and self.rightChild

    # Replace a node completely. Its keym payload, and children.
    # Remember to make sure the children knows its parent
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        # Assign the node itself as the parent of its children
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
