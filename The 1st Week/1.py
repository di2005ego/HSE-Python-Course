#https://leetcode.com/problems/longest-substring-without-repeating-characters/
s = str(input())
count = 0
l = 0
set = set()
for r in range(len(s)):
    rChar = s[r]
    while rChar in set:
        lChar = s[l]
        set.remove(lChar)
        l += 1
    set.add(rChar)
    counter = max(counter, r - l + 1)
lengthOfLongestSubstring = counter
print(lengthOfLongestSubstring)

'''
Решение в LeetCode
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
'''