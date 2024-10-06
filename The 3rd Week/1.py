#https://leetcode.com/problems/container-with-most-water/


class Solution(object):
    def maxArea(self, height):
        answer, i, j = 0, 0, len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                result = height[i] * (j - i)
                i += 1
            else:
                result = height[j] * (j - i)
                j -= 1
            if result > answer:
                answer = result
        return answer