# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/


class Solution(object):
    def minKBitFlips(self, nums, k):
        length = len(nums)
        flips = [0] * (length + 1)
        total_flips = 0
        flip_counter = 0
        for index, val in enumerate(nums):
            flip_counter += flips[index]
            if (val + flip_counter) % 2 == 0:
                if index + k > length:
                    return -1
                flips[index] += 1
                flips[index + k] -= 1
                flip_counter += 1
                total_flips += 1
        return total_flips
