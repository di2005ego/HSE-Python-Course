#https://leetcode.com/problems/3sum-closest/


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[n - 1]
        for i in range(0, n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum <= target:
                    j += 1
                else:
                    k -= 1
                if abs(closest - target) > abs(currentSum - target):
                    closest = currentSum
        return closest