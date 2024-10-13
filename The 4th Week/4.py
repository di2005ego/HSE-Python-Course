# https://leetcode.com/problems/combination-sum/


class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(index, currSum):
            if currSum == 0:
                combinations.append(combinationSoFar[:])
                return
            if index >= len(candidates) or currSum < candidates[index]:
                return
            dfs(index + 1, currSum)
            combinationSoFar.append(candidates[index])
            dfs(index, currSum - candidates[index])
            combinationSoFar.pop()

        candidates.sort()
        combinationSoFar = []
        combinations = []
        dfs(0, target)
        return combinations
