# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = []
        current_level = [root]
        left_to_right = True
        while current_level:
            level_values = []
            next_level = []
            for node in current_level:
                level_values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if not left_to_right:
                level_values.reverse()
            result.append(level_values)
            current_level = next_level
            left_to_right = not left_to_right
        return result
