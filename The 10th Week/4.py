# https://leetcode.com/problems/binary-tree-level-order-traversal/


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
