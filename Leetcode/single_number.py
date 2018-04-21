# Problem:  136. Single Number

from collections import defaultdict

def singleNumber (nums):
    hashTable = defaultdict(int)
    for i in nums:
        hashTable[i] += 1
    for k in hashTable.keys():
        if hashTable[k] == 1:
            return k

singleNumber([4,1,2,1,2])
