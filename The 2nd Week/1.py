#https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        rows, cols = (len(s), len(p))
        dp = [[False for j in range(cols + 1)] for i in range(rows + 1)]
        dp[0][0] = True
        for i in range(2, cols + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif j > 1 and p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[rows][cols]