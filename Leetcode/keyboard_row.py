'''
Problem Info:

Website:       Leetcode
Problem Name:  500. Keyboard Row

Problem:
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

Solution:
Create a list of sets to represent each row of the keyboard. Check which row
first letter is in. Then check which row every other letter is in.

Time complexity: O(n)
Space complexity: (1)
'''

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
    def findWords(self, words):
        keyboard_rows = [{'Q','W','E','R','T','Y','U','I','O','P'},
                        {'A','S','D','F','G','H','J','K','L'},
                        {'Z','X','C','V','B','N','M'}]
        out = []

        for word in words:
            word_upper = word.upper()
            add_word = True

            for i in range(len(keyboard_rows)):
                if word_upper[0] in keyboard_rows[i]:
                    row = i

            for letter in word_upper:
                if not (letter in keyboard_rows[row]):
                    add_word = False

            if add_word:
                out.append(word)

        return out
