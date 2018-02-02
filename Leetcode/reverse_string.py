'''
Problem Info:

Website:       Leetcode
Problem Name:  344. Reverse String

Problem:
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Solution:
Three approaches below.

Time complexity: O(n)
Space complexity: (1)
'''

# using Python's built in slicing option
class Solution:
    def reverseString (self, s):
        return s[::-1]


# Iterative Solution
class Solution1:
    def reverseString(self, s):
        start = 0
        end = len(s) - 1
        i = 0
        outstring = ""

        for letter in s:
            outstring += s[end-i]
            i+=1

        return outstring


# Recursive solution
class Solution2:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        else:
            return s[-1] + self.reverseString(s[:-1])
