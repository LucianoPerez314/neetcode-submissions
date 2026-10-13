# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # same principle as the last problem:
        # every entry in the frontier stores it's level a.k.a distance from root.

        # at the boundary where the level changes is our right most node at that level.
        if root is None:
            return []
        
        frontier = [(root, 0)]
        res = []
        prev, prev_lvl = None, -1
        while True:
            curr, lvl = frontier.pop(0)
            if curr.left is not None:
                frontier.append((curr.left, lvl+1))
            if curr.right is not None:
                frontier.append((curr.right, lvl+1))
            if prev is not None and prev_lvl == lvl - 1:
                res.append(prev.val)

            if len(frontier) == 0:
                res.append(curr.val)
                break
            prev, prev_lvl = curr, lvl
        return res
            
            




        