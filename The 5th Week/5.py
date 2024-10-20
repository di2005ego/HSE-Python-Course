# https://leetcode.com/problems/word-break/


class Solution(object):
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            dp[i] = any((dp[j] and s[j:i] in words) for j in range(i))
        return dp[n]
