# link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(current_node):
            if current_node is None:
                return 0 

            left = traverse(current_node.left)
            right = traverse(current_node.right)

            return max(left, right) + 1
        
        return traverse(root)

        