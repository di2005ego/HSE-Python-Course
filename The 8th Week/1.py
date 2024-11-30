# https://leetcode.com/problems/binary-subarrays-with-sum/


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        left1 = left2 = sum1 = sum2 = idx = total_subarrays = 0
        array_length = len(nums)
        while idx < array_length:
            sum1 += nums[idx]
            sum2 += nums[idx]
            while left1 <= idx and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            while left2 <= idx and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            total_subarrays += left2 - left1
            idx += 1
        return total_subarrays
