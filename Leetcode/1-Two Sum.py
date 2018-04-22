from collections import defaultdict

def twoSum(nums, target):
    dict = defaultdict(int)

    for i, num in enumerate(nums):
        dict[num] = i

    for i, num in enumerate(nums):
        second = target-num
        # Second check is to ensure that same element is not used twice
        if second in dict and dict[second] != i:
            return [i, dict[second]]
