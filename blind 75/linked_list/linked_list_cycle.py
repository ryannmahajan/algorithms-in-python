# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        one_stepper, two_stepper = head, head
        while two_stepper is not None and two_stepper.next is not None:
            one_stepper = one_stepper.next
            two_stepper = two_stepper.next.next

            if two_stepper is not None:
                if one_stepper == two_stepper: return True
        
        return False