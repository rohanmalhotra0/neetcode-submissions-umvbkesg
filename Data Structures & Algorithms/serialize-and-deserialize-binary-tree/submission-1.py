# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N": # Base Case Leaf ends
                self.i += 1         # Increment i and return none
                return None
            node = TreeNode(int(vals[self.i])) # Combination Step create a treenode and cast str vals[i] as an int
            self.i += 1                        # Increment i
            node.left = dfs()                  # DFS on Left
            node.right = dfs()                 # DFS on Right
            return node                        # Return the node added to the tree

        return dfs()                           # Return The Root of the Tree just call DFS where i = 0 