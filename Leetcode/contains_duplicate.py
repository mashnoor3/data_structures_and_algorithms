# 217. Contains Duplicate
from collections import defaultdict

def containsDuplicate(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    for k in dict.keys():
        if dict[k] > 1:
            return True
    return False

containsDuplicate([1,2,3,4,5])
containsDuplicate([1,2,3,4,5,6,3,4])
