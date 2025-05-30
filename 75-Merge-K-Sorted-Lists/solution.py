# link: https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(sll1, sll2):
    if sll1 is None or sll2 is None:
        return sll2 if sll2 else sll1
    temp1 = sll1
    temp2 = sll2
    new_sll = None
    prev = None
    while temp1 and temp2:
        if temp1.val < temp2.val:
            if new_sll is None:
                new_sll = ListNode(val=temp1.val)
                prev = new_sll
            else:
                prev.next = ListNode(val=temp1.val)
                prev = prev.next
            temp1 = temp1.next
        else:
            if new_sll is None:
                new_sll = ListNode(val=temp2.val)
                prev = new_sll
            else:
                prev.next = ListNode(val=temp2.val)
                prev = prev.next
            temp2 = temp2.next
    
    while temp1:
        prev.next = ListNode(val=temp1.val)
        prev = prev.next
        temp1 = temp1.next
            
    while temp2:
        prev.next = ListNode(val=temp2.val)
        prev = prev.next
        temp2 = temp2.next
        
    return new_sll


def merge_sort(my_list):
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list[0]
        
    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])
    return merge(left, right)

   
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return merge_sort(lists)