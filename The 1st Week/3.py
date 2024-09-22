#https://leetcode.com/problems/zigzag-conversion

class Solution(object):
    def convert(self, s, numRows):
        n = len(s)
        if numRows == 1:
            return s
        res = ""
        step = 2*numRows-2
        for i in range (0, numRows):
            for j in range (i, len(s), step):
                res += s[j]
                if i != 0 and i != numRows - 1 and (j + step - 2*i) < n:
                    res+=s[j + step - 2*i]
        return res