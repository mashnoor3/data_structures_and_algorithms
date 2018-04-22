from collections import defaultdict

# Using lists. Lookup with lists is O(n), so overall algorithm runtime is O(n^2)
def intersect2(nums1,nums2):
    output = []
    for num in nums1:
        if num in nums2:
            output.append(num)
            nums2.remove(num)
    return output

# Using dictionary. Lookup with dicts is O(1), so overall algorithm runtime is O(n)
def intersect(nums1,nums2):
    output, dict1 = [], defaultdict(int)
    for num in nums1:
        dict1[num] += 1

    for n in nums2:
        print(n)
        if dict1[n] > 0:
            dict1[n] -= 1
            output.append(n)
    return output
