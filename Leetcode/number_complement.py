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

Time complexity: O(log(n))
Space complexity: O(1)
'''


# Solution using Python's bitwise operators
class Solution:

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        # Only need to create binary number to XOR is it's 2 or more bits
        if num > 1:
            # Create a binary number that is the same number of bits as num
            while i <= num:
                i = i << 1
            # Subtract 1 to make binary number all ones
            i = i - 1

        # XOR i with num to flip the bits for num
        return num ^ i

# Alternative solution without using Python's bitwise operators
class Solution2:

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
