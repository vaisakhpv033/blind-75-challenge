# link: https://leetcode.com/problems/reorder-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d_que = deque([])
        temp = head
        while temp:
            node = temp
            temp = temp.next
            node.next = None
            d_que.append(node)
        if d_que:
            temp = d_que.popleft()
        n = len(d_que)
        i = 0
        while i < n:
            temp.next = d_que.pop()
            temp = temp.next
            i += 1
            if i < n:
                temp.next = d_que.popleft()
                temp = temp.next
                i += 1

# time complexity: O(n)
# space complexity: O(n)

