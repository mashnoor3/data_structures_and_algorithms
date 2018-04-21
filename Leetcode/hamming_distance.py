'''
Problem Info:

Website:       Leetcode
Problem Name:  461. Hamming Distance

Problem:
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Solution:
Idea:               Convert each integer to binary. Then iterate and compare.
Time complexity:    O(n)
Space complexity:   O(n)
'''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = self.dec_to_bin(x)
        y_bin = self.dec_to_bin(y)

        # Need to normalize the binary representations to ensure they have the
        # same number of bits
        if len(x_bin) > len(y_bin):
            while not (len(y_bin) == len(x_bin)):
                y_bin.insert(0,0)
        else:
            while not (len(y_bin) == len(x_bin)):
                x_bin.insert(0,0)

        hd = 0
        for i in range(len(x_bin)):
            if not (x_bin[i] == y_bin[i]):
                hd += 1

        return hd

    def dec_to_bin(self, dec):
        quotient = dec
        # Binary number will be represented as a queue
        binary = []

        # Convert from dec to bin. Use integer division, and modulo by 2.
        while not (quotient == 0):
            quotient = dec // 2
            remainder = dec % 2

            binary.insert(0,remainder)

            dec = quotient

        return binary
