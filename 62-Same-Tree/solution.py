# link: https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs_traversal(node):
            result = []
            def traverse(node):
                if node is None:
                    result.append(None)
                else: 
                    result.append(node.val)
                    traverse(node.left)
                    traverse(node.right)
            traverse(node)
            return result
        first_tree = dfs_traversal(p)
        second_tree = dfs_traversal(q)
        return first_tree == second_tree
        