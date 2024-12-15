# https://leetcode.com/problems/unique-binary-search-trees-ii/


class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.tree_constructor(1, n)

    def tree_constructor(self, start, end):
        results = []
        if start > end:
            results.append(None)
            return results
        for i in range(start, end + 1):
            left_trees = self.tree_constructor(start, i - 1)
            right_trees = self.tree_constructor(i + 1, end)
            for left in left_trees:
                for right in right_trees:
                    current_node = TreeNode(i)
                    current_node.left = left
                    current_node.right = right
                    results.append(current_node)
        return results
