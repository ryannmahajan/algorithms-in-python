# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = find_length(head)
        if length==1: return None

        to_remove = length - n
        curr = head
        for i in range(to_remove):
            curr = curr.next

        curr.next = curr.next.next

def find_length(head):
    res = 0
    curr = head

    while curr:
        curr = curr.next
    
    return res

        