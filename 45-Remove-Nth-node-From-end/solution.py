# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head 
        while temp:
            length += 1
            temp = temp.next
        prev, temp = None, head
        count, target = 0, length - n
        while temp:
            if count == target:
                if temp is None:
                    return head
                elif prev is None:
                    return temp.next
                else:
                    prev.next = temp.next
            count += 1
            prev, temp = temp, temp.next
        return head
        
# time complexity: O(n)
# space complexity: O(1)

        