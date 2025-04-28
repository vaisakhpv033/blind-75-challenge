# link: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        j = 0
        temp1, temp2 = list1, list2
        len_list1, len_list2 = self.length(list1), self.length(list2)
        prev = None
        head = None
        while i < len_list1 and j < len_list2:
            if temp1.val < temp2.val:
                if prev is None:
                    prev = temp1
                    temp1 = temp1.next
                    prev.next = None
                    head  = prev
                else:
                    prev.next = temp1
                    prev = prev.next
                    temp1 = temp1.next
                    prev.next = None
                i += 1
            else:
                if prev is None:
                    prev = temp2
                    temp2 = temp2.next
                    prev.next = None
                    head = prev
                else:
                    prev.next = temp2
                    prev = prev.next
                    temp2 = temp2.next
                    prev.next = None
                j += 1
        
        while i < len_list1:
            if prev is None:
                return list1
            else:
                prev.next = temp1
                prev = prev.next
                temp1 = temp1.next
                prev.next = None
            i += 1

        while j < len_list2:
            if prev is None:
                return list2
            else:
                prev.next = temp2
                prev = prev.next
                temp2 = temp2.next
                prev.next = None
            j += 1
        return head
        



    def length(self, list1):
        temp = list1
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length
        
# time complexity: O(n) where n is the len(list1) + len(list2)
# space complexity: O(1)