class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSameTree(root, subRoot) or \
            self.isSameTree(root.left, subRoot) or \
            self.isSameTree(root.right, subRoot)

    def isSameTree(self, p, q) -> bool:
        if (p is None) and (q is None): return True
        elif (p is None) or (q is None): return False
        print(f"Comparing {p} and {q}")

        return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

# a = TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= None, right= TreeNode{val= 1, left= TreeNode{val= 2, left= None, right= None}, right= None}}}}}}}}}}}