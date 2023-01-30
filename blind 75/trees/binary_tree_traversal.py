# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        res.append([root.value])

        self.level_order_helper(root, res)

        return res
    
    def level_order_helper(self, root, res, level=1):
        if (root.left or root.right) and len(res) < level + 1:
            res.append([])
        if root.left:
            res[level].append(root.left.value)
        if root.right:
            res[level].append(root.right.value)

        if root.left: self.level_order_helper(root.left, res, level + 1)
        if root.right: self.level_order_helper(root.right, res, level + 1)

        
        
