#https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        check = len(s) >= 1
        if check == False:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s=s.lstrip()
        isNeg = len(s) > 1 and s[0] == '-'
        isPos = len(s) > 1 and s[0] == '+'
        num = 0
        i = 0
        if isNeg or isPos:
            i += 1
        while i < len(s) and '0' <= s[i] <= '9':
            num = num*10 + (ord(s[i])-ord('0'))
            i += 1
        if isNeg:
            num = -num
        if num < INT_MIN:
            num = INT_MIN
        if num > INT_MAX:
            num = INT_MAX
        return num