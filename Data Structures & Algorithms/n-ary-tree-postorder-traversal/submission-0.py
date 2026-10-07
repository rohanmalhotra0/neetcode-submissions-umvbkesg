"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            for child in node.children:
                dfs(child)
            res.append(node.val)

        dfs(root)
        return res

        '''
        return res
        q.append([root])
        seen = set()
        seen.add(root)
        while q:
            node = q.popleft()
            for nei in node.children:
                if nei in seen:
                    continue
                q.append(nei)             
                seen.add(nei)




                '''