#https://leetcode.com/problems/4sum/


class Solution(object):
    def fourSum(self, nums, target):
        quadruplets = list()
        if len(nums) < 4:
            return quadruplets
        nums.sort()
        n = len(nums)
        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    currentSum = nums[i] + nums[j] + nums[k] + nums[l]
                    if currentSum < target:
                        k += 1
                    elif currentSum > target:
                        l -= 1
                    else:
                        quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return quadruplets
