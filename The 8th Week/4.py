# https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution(object):
    def longestOnes(self, nums, k):
        left = right = -1
        while right < len(nums) - 1:
            right += 1
            if nums[right] == 0:
                k -= 1
            if k < 0:
                left += 1
                if nums[left] == 0:
                    k += 1
        return right - left
