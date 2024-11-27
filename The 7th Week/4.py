# https://leetcode.com/problems/maximum-length-of-repeated-subarray/


class Solution(object):
    def findLength(self, nums1, nums2):
        length_nums1, length_nums2 = len(nums1), len(nums2)
        dp_table = [[0] * (length_nums2 + 1) for _ in range(length_nums1 + 1)]
        max_length = 0
        for i in range(1, length_nums1 + 1):
            for j in range(1, length_nums2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                    max_length = max(max_length, dp_table[i][j])
        return max_length
