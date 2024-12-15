# https://leetcode.com/problems/recover-binary-search-tree/


class Solution(object):
    def recoverTree(self, root):
        self.first_swapped = None
        self.second_swapped = None
        self.prev_node = None

        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            if self.prev_node and self.prev_node.val > node.val:
                if not self.first_swapped:
                    self.first_swapped = self.prev_node
                self.second_swapped = node
            self.prev_node = node
            inorder_traversal(node.right)

        inorder_traversal(root)
        if self.first_swapped and self.second_swapped:
            self.first_swapped.val, self.second_swapped.val = (
                self.second_swapped.val,
                self.first_swapped.val,
            )
