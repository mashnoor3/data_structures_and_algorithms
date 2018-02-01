'''
Problem Info:

Website:       Leetcode
Problem Name:  476. Number Complement

Problem:
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Solution:
Convert the integer to binary, this will be a stack.
XOR every bit (digit) oin the binary number (stack).
Convert from binary back to decimal.

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:

    def bin_to_dec(self, bin_list):
        num = 0
        for i, digit in enumerate(bin_list):
            num = num + digit*pow(2,i)
        return num

    def dec_to_bin(self, dec):
        quot = dec
        rem = dec
        # Represent binary number as a stack. So in reverse order. This is useful
        # when reverting back from binary to decimal
        binary = []
        while quot > 0:
            rem = quot % 2
            binary.append(rem)

            quot = quot // 2
        return binary

    def xor(self, bin_list):
        for i, digit in enumerate(bin_list):
            if digit == 0:
                bin_list[i] = 1
            else:
                bin_list[i] = 0
        return bin_list

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return  self.bin_to_dec(self.xor(self.dec_to_bin(num)))
