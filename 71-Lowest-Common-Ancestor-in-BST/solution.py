# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val in [p.val, q.val]:
                return node
            elif p.val > node.val and q.val < node.val:
                return node
            elif p.val < node.val and q.val > node.val:
                return node
            else:
                if p.val > node.val:
                    node = node.right
                else:
                    node = node.left
        