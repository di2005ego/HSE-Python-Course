# https://leetcode.com/problems/find-k-closest-elements/


class Solution(object):
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left : left + k]
