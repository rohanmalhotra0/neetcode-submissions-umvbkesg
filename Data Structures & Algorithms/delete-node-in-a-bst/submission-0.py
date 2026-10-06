# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Found the node
        else:
            # Case 1: no left child
            if not root.left:
                return root.right

            # Case 2: no right child
            if not root.right:
                return root.left

            # Case 3: two children
            successor = root.right

            # Find smallest value in right subtree
            while successor.left:
                successor = successor.left

            # Copy successor value into current node
            root.val = successor.val

            # Delete the duplicate successor
            root.right = self.deleteNode(root.right, successor.val)

        return root