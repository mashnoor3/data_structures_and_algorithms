from collections import defaultdict

def topKFrequent(nums, k):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1

    out = []
    for key in dict.keys():
        if dict[key] >= k:
            out.append(key)
    return out

print(topKFrequent([1,1,1,2,2,3],2))
