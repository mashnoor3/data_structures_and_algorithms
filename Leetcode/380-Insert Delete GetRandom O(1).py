from collections import defaultdict
import random

class RandomizedSet:

    def __init__(self):
        self.myList, self.myDict = [], defaultdict(int)


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myDict:
            return False
        else:
            myDict[val] += 1
            myList.append(val)
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myDict:
            del myDict[val]
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.myDict) == 0:
            return False

        return random.choice(list(self.myDict.keys()))
