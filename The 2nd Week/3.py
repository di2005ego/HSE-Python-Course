#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        chars = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for digit in digits:
            digit = int(digit)
            temp = []
            for char in chars[digit]:
                for word in res:
                    word += char
                    temp.append(word)
            res = temp
        return res