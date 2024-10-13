# https://leetcode.com/problems/jump-game-ii/


class Solution(object):
    def jump(self, nums):
        jumpCount = maxReach = lastReach = 0
        for index, val in enumerate(nums[:-1]):
            maxReach = max(maxReach, index + val)
            if lastReach == index:
                jumpCount += 1
                lastReach = maxReach
        return jumpCount
