'''
Problem Info:

Website:        Leetcode
Problem Name:  760. Find Anagram Mappings

Problem:
Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B
is made by randomizing the order of the elements in A.
We want to find an index mapping P, from A to B. A mapping P[i] = j means
the ith element in A appears in B at index j.
These lists A and B may contain duplicates.
If there are multiple answers, output any of them.

Solution:
Idea:               Use a Hash table for look up, and array for returning.
Time complexity:    O(n)
Space complexity:   O(n)
'''

import collections

class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ht = collections.defaultdict(int)
        mapping = []

        # Iterate through B and add items to hash table. Key is the data of of B
        for i in range(len(B)):
            ht[B[i]] = i

        # Iterate through A, obtain values from hash table using A[i] as the key
        for j in range(len(A)):
            mapping.append(ht[A[j]])

        return mapping
