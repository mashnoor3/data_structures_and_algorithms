'''
Problem Info:

Website:       Leetcode
Problem Name:  728. Self Dividing Numbers

Problem:
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible.

Solution:
Idea:
Iterate through each number in the range, and call helper function to see if that
number is self diving. If so, then append to output list.

Time complexity: O(n^2)
Space complexity: O(n)
'''

"""
:type left: int
:type right: int
:rtype: List[int]
"""
class Solution:
    def is_self_dividing(self, input_num):
        # Quotient is eesnetially temp variable to calculate the current digit
        quotient = input_num
        check = True

        while quotient > 0 and check:
            # Remainder is the current digit to divide by
            remainder = quotient % 10

            # If not dovisible by the current digit, or if current digit is 0
            # will return false
            if remainder == 0 or not(input_num % remainder == 0):
                check = False

            # Update quotient
            quotient = quotient // 10

        return check

    def selfDividingNumbers(self, left, right):
        # Make List for input and output. List comprehension for input list
        input_list = [num for num in range(left, right+1)]
        output_list = []

        # Iterate through the List
        for i in input_list:
            if self.is_self_dividing(i):
                output_list.append(i)

        return output_list
