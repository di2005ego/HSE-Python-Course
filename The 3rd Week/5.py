#https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        l = 0
        r = m
        while l <= r:
            partition1 = (l + r) // 2
            partition2 = (m + n + 1) // 2 - partition1
            if partition1 == 0:
                maxLeft1 = -(2**31)
            else:
                maxLeft1 = nums1[partition1 - 1]
            if partition2 == 0:
                maxLeft2 = -(2**31)
            else:
                maxLeft2 = nums2[partition2 - 1]
            if partition1 == m:
                minRight1 = 2**31 - 1
            else:
                minRight1 = nums1[partition1]
            if partition2 == n:
                minRight2 = 2**31 - 1
            else:
                minRight2 = nums2[partition2]
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                r = partition1 - 1
            else:
                l = partition1 + 1
