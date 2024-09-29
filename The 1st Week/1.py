#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        finalCounter = 0
        l = 0
        arr = set()
        for r in range(len(s)):
            rChar = s[r]
            while rChar in arr:
                lChar = s[l]
                arr.remove(lChar)
                l += 1
            arr.add(rChar)
            finalCounter = max(finalCounter, r - l + 1)
        lengthOfLongestSubstring = finalCounter
        return lengthOfLongestSubstring