'''
Problem Info:

Website:       Leetcode
Problem Name:  557. Reverse Words in a String III

Problem:
Given a string, you need to reverse the order of characters in each word within
a sentence while still preserving whitespace and initial word order.

Solution:
Helper function to reverse leters in a word. Iterate through each word in the
input string, and call reverse_word().

Time complexity: O(n)
Space complexity: (1)
'''

class Solution:

    def reverse_word(self, word):
        # Base Case. Remember to account for empty string. Therefore size 1 or 0
        if len(word) <= 1:
            return word
        # Recursive Case
        else:
            return word[-1] + self.reverse_word(word[:-1])

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split(" ")
        output_str = ""

        for i, word in enumerate(word_list):
            output_str += self.reverse_word(word)
            # Only add a space if not at the last word
            if not (i == len(word_list) -1):
                output_str += " "

        return output_str
