# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 5
# 4 6
# 4 3 7
# 4 3 
# 4 
# 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # right inherits previous as lower limit
        # left inherits previous as upper limit
        # if falls outside of bounds return false.
        # each node has their own respective lower and upper limit.
        if root is None:
            return True

        frontier = [(root, float("-inf"), float('inf'))]
        while len(frontier) != 0:
            current, lower_lim, upper_lim = frontier.pop()

            if current.val <= lower_lim or current.val >= upper_lim:
                return False

            if current.left is not None:
                frontier.append((current.left,lower_lim,current.val))
            if current.right is not None:
                frontier.append((current.right,current.val,upper_lim))
        return True
        
        