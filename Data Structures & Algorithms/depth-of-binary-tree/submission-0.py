# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return remainingDepth(root, 0)
        
def remainingDepth(root, depthSoFar):
    if root == None:
        return depthSoFar
    depthl = remainingDepth(root.left, depthSoFar+1)
    depthr = remainingDepth(root.right, depthSoFar+1)
    return max(depthl, depthr)
        