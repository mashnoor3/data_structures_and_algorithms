from collections import defaultdict
from heapq import heappush, heappop, nlargest

def topKFrequent(nums, k):
    hashTable, heap = defaultdict(int), []

    for num in nums:
        hashTable[num] += 1

    # O(n*log(n)) time complexity to create heap
    for ele in hashTable.keys():
        # Create heap where the keys are the values from hashtable
        heappush(heap, (hashTable[ele], ele))

    # Tuple unpacking to separate key and value of heap nodes
    occurrence, ele = zip(*nlargest(k, heap))

    return list(ele)

print(topKFrequent([1,1,1,2,2,4],2))
