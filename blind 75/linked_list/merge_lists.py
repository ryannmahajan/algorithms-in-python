# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head1, head2 = list1, list2

        new_list = get_less_val_node(head1, head2)
        head_new_list = new_list

        while head1 is not None and head2 is not None:
            
            if head1.val < head2.val:
                new_list.next = head1
                head1 = new_list.next.next
            else:
                new_list.next = head2
                head2 = new_list.next.next

            new_list = new_list.next
        
        if head1 is None:
            new_list.next = head2
        if head2 is None:
            new_list.next = head1
        
        return head_new_list

def get_less_val_node(head1, head2):
    if head1.val < head2.val:
        return head1
    return head2

list1 = [1,2,4]
list2 = [1,3,4]
Solution().mergeTwoLists(list1, list2)