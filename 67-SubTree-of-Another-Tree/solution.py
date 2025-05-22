# link: https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def traverse(r, s):
            value = self.sametree(r, s)
            if not value and r:
                value = traverse(r.left, s)
                if not value:
                    value = traverse(r.right, s)
            return value
        return traverse(root, subRoot)

    
    def sametree(self, t, s):
        if t is None and s is None:
            return True
        elif t is None and s is not None:
            return False
        elif s is None and t is not None:
            return False
        
        if t.val != s.val :
            return False

        left = self.sametree(t.left, s.left)
        right = False
        if left:
            right = self.sametree(t.right, s.right)

        return right
            