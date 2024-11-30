# https://leetcode.com/problems/longest-turbulent-subarray/


class Solution(object):
    def maxTurbulenceSize(self, arr):
        max_length = increasing = decreasing = 1
        for i in range(len(arr) - 1):
            current, next_element = arr[i], arr[i + 1]
            temp_inc = decreasing + 1 if current < next_element else 1
            temp_dec = increasing + 1 if current > next_element else 1
            increasing, decreasing = temp_inc, temp_dec
            max_length = max(max_length, increasing, decreasing)
        return max_length
