'''
Problem Info:

Website:       Leetcode
Problem Name:  657. Judge Route Circle

Problem:
Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a
character. The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Solution:
Idea:               Iterate through each letter of string, and update counters.
Time complexity:    O(n)
Space complexity:   O(1)
'''

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up_down = 0
        down = 0
        left = 0
        right = 0

        for i in moves:
            if i == 'U':
                up += 1
            if i == 'D':
                down += 1
            if i == 'R':
                right += 1
            if i == 'L':
                left += 1

        if up == down and left == right:
            return True
        else:
            return False
