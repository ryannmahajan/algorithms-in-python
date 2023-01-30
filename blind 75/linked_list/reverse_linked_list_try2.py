# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if (head is None or head.next is None): return head

        new_head = self.reverseList(head.next)

        prev_next = head.next
        prev_next.next = head

        return new_head
        
        
        

        
        