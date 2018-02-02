'''
Problem Info:

Website:       Leetcode
Problem Name:  682. Baseball Game

Problem:
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Solution:
Use a stack to keep track of all previous points. Iterate through list updating
stack and sum.

Time complexity:    O(n)
Space complexity:   O(n)
'''

class Solution:
    def calPoints (self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # Use a stack to represent the previous points
        prev_pts = []
        out = 0

        for i in ops:
            if i == 'C':
                invalid_pt = prev_pts.pop()
                out -= invalid_pt
            elif i == 'D':
                double_pt = 2*prev_pts[-1]
                prev_pts.append(double_pt)
                out += double_pt
            elif i == '+':
                sum_last_two = prev_pts[-1] + prev_pts [len(prev_pts)-2]
                prev_pts.append(sum_last_two)
                out += sum_last_two
            else:
                prev_pts.append(int(i))
                out += prev_pts[-1]

        return out
