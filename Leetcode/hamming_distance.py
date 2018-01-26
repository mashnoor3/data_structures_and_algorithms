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

def hammingDistance(x, y):

        x_bin = dec_to_bin(x)
        y_bin = dec_to_bin(y)

        if len(x_bin) > len(y_bin):
            max_length = len(x_bin) - 1
        else:
            max_length = len(y_bin) - 1

        hd = 0

        for i in range(max_length):
            if not (x_bin[i] == y_bin[i]):
                hd += 1

        print (hd)
        return hd

def dec_to_bin(dec):
    quotient = dec
    # Binary represented as a ___
    binary = []

    while not (quotient == 0):
        quotient = dec // 2
        remainder = dec % 2

        binary.insert(0,remainder)

        dec = quotient

    # print(binary)
    return binary

hammingDistance(7,8)
