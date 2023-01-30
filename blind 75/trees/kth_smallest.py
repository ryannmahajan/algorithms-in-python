# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        popped = 0
        stack = []
        curr = root

        while curr is not None or len(stack) > 0:
            if curr:
                stack.append(curr)
                curr = curr.left
                continue
            
            curr = stack.pop()
            popped+=1
            if popped==k:
                return curr.val
            
            curr = curr.right
            # if curr.right:
            #     stack.append(curr.right)

        
        
