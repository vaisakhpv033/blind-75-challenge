# link: https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = head.next
        next_node = ListNode(head.val)
        while temp:
            new_node = ListNode(temp.val, next_node)
            next_node = new_node
            temp = temp.next
        return next_node

# time complexity: O(n)
# space complexity: O(n)


            