# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val==p.val or root.val==q.val:
            return root
        
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

        # if self.contains(root.left, p) and self.contains(root.left, q):
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif self.contains(root.right, p) and self.contains(root.right, q):
        #     return self.lowestCommonAncestor(root.right, p, q)
        
        # return root
    
    def contains(self, root, to_find):
        if root.val < to_find.val:
            return True if root.right is not None else False
        elif root.val > to_find.val:
            return True if root.left is not None else False

        return True
        
