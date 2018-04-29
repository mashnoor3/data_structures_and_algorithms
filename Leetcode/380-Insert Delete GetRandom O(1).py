from collections import defaultdict
import random

# Use a dictionary for O(1) insert and remove, and List for O(1) getRandom
# Dict. Key is the item, and value is position in list
# For list pop of end is O(1), and then copy over also O(1)

class RandomizedSet:
    def __init__(self):
        self.myList, self.myDict = [], defaultdict(int)

    def insert(self, val):
        if val in self.myDict:
            return False
        self.myList.append(val)
        pos = len(self.myList)-1
        self.myDict[val] = pos
        return True

    def remove(self, val):
        if val not in self.myDict:
            return False
        if len(self.myList) == 1:
            del self.myDict[val]
            self.myList.pop()
        else:
            pos = self.myDict[val]
            del self.myDict[val]
            tmp = self.myList.pop()
            # If removed item from middle of list,
            # then need to swap the popped element into correct index
            if tmp != val:
                self.myList[pos] = tmp
                self.myDict[tmp] = pos
        return True

    def getRandom(self):
        if len(self.myList) == 0:
            return False
        i = random.randint(0,len(self.myList)-1)
        return self.myList[i]

    def printBoth (self):
        print (self.myList)
        print (self.myDict)
