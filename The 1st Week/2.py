#https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        s1 = []
        for i in s:
            s1.append(i)
            s1.append("|")
        c = 0
        m = len(s1)
        palRad = [0]*m
        while c < m:
            r = 0
            while c - (r + 1) >= 0 and c + (r + 1) < m and s1[c-(r+1)] == s1[c+(r+1)]:
                r += 1
            palRad[c] = r
            c += 1
        longPal = max(palRad)
        index = palRad.index(max(palRad))
        if index % 2 != 0:
            sindex = (index + 1) // 2
            value = (longPal + 1) // 2
            return s[sindex - value : sindex + value]
        else:
            sindex = index // 2
            value = longPal // 2
            return s[sindex - value : sindex + value + 1]