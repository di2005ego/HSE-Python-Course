# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution(object):
    def searchRange(self, nums, target):
        l = bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            return -1, -1
        r = bisect_right(nums, target) - 1
        return l, r
