# link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        node = TreeNode(preorder[0])
        for idx, val in enumerate(inorder):
            if val == node.val:
                split_idx = idx
                break
        left_in, right_in = inorder[:split_idx], inorder[split_idx+1:] 
        m, n = len(left_in), len(right_in)
        left_pre, right_pre = preorder[1: m+1], preorder[m+1:]
        
        node.left = self.buildTree(left_pre, left_in)
        node.right = self.buildTree(right_pre, right_in)

        return node