# link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        output = []
        q.append(root)
        while len(q) > 0:
            new = [] 
            idx = len(q)
            while idx > 0:
                node = q.popleft()
                new.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                idx -= 1
            output.append(new)
        return output
