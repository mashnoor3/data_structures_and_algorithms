'''
Problem Info:

Website:       Leetcode
Problem Name:  766. Toeplitz Matrix

Problem:
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Notes:
matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Solution:


Time complexity: O(m*n)
Space complexity: O(1)
'''

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # If just one row or just one col, then only has one diagonal for each
        if len(matrix) == 0 or len(matrix[0])==0:
            return True

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row and col > 0:
                    # Check diagonal of an element bu cehcking row-1, col-1
                     # If not the same, then return false
                    if not (matrix[row][col] == matrix [row-1][col-1]):
                        return False
        return True
