'''
Idea:
Iterate over every element in the board, and add to hashtable.
One hashtable for each check; row, col, box.
Use belper function to map r,c to a box number.
'''

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r_ht = [{},{},{},{},{},{},{},{},{}]
        c_ht = [{},{},{},{},{},{},{},{},{}]
        box_ht = [{},{},{},{},{},{},{},{},{}]

        for r in range(len(board)):
            for c in range (len(board[0])):
                curr = board[r][c]
                box = self.getBoxNumber(r,c)
                if curr == '.':
                    pass
                # Check row and column for the current element
            elif curr in r_ht[r] or curr in c_ht[c]:
                    return False
                # Check box for the current element
            elif curr in box_ht[box]:
                    return False
                # Add element
                else:
                    r_ht[r][board[r][c]] = 1
                    c_ht[c][board[r][c]] = 1
                    box_ht[box][curr] = 1
        return True

    # Return the box number which is between 0-8
    def getBoxNumber(self, r, c):
        b = 3*(r//3) + c//3
        return b
