# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if not node1 and not node2:
                return True
            if p and q and node1.val == node2.val:
                return equal(p.left, q.left) and equal(p.right, q.right)
            else:
                return False
        
        if not subRoot:
            return True
        if not root:
            return False

        if self.equal(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))