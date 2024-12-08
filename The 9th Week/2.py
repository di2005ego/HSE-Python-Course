# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


class Solution(object):
    def sortedListToBST(self, head):
        curr, count = head, 0
        while curr:
            curr = curr.next
            count += 1

        def treeify(i, j):
            if j < i:
                return None
            mid, node = i + j >> 1, TreeNode()
            node.left = treeify(i, mid - 1)
            node.val, curr[0] = curr[0].val, curr[0].next
            node.right = treeify(mid + 1, j)
            return node

        curr = [head]
        return treeify(1, count)
