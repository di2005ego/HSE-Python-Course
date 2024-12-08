# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


class Solution(object):
    def connect(self, root):
        if root is None:
            return root
        queue = deque([root])
        while queue:
            previous_node = None
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if previous_node:
                    previous_node.next = node
                previous_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
