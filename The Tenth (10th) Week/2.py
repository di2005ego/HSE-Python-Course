# https://leetcode.com/problems/validate-binary-search-tree/


class Solution(object):
    def isValidBST(self, root):
        def validate(node, low=float("-inf"), high=float("inf")):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root)
