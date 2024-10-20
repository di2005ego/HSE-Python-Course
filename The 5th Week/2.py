# https://leetcode.com/problems/set-matrix-zeroes/


class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        i_zero = any(v == 0 for v in matrix[0])
        j_zero = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if i_zero:
            for j in range(n):
                matrix[0][j] = 0
        if j_zero:
            for i in range(m):
                matrix[i][0] = 0
