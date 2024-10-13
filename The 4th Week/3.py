# https://leetcode.com/problems/valid-sudoku/


class Solution(object):
    def isValidSudoku(self, board):
        rows = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cellValue = board[i][j]
                if cellValue == ".":
                    continue
                num = int(cellValue) - 1
                boxIndex = (i // 3) * 3 + j // 3
                if rows[i][num] or columns[j][num] or boxes[boxIndex][num]:
                    return False
                rows[i][num] = True
                columns[j][num] = True
                boxes[boxIndex][num] = True
        return True
