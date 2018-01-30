'''
Problem Info:

Website:       Leetcode
Problem Name:  771. Jewels and Stones

Problem:
ou're given strings J representing the types of stones that are jewels, and S
representing the stones you have.  Each character in S is a type of stone you
have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are
letters. Letters are case sensitive, so "a" is considered a different type of
stone from "A".

Solution:
Idea:

Time complexity:    O(n) (need to go through all nodes)
Space complexity:   O(logn) for average case, and O(n) for worst case (skewed tree)
'''

import collections

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        jewels_ht = collections.defaultdict(int)

        for jewel in J:
            jewels_ht[jewel] = 0

        num_jewels = 0

        for stone in S:
            if stone in jewels_ht:
                jewels_ht[stone] += 1
                num_jewels += 1

        return num_jewels
