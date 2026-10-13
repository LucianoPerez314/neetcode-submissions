# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = determineDepth(root, 0, 0)
        return diameter

def determineDepth(root, depthSoFar, res):
    if root == None:
        return 0, res
    max_depth1, res = determineDepth(root.left, depthSoFar + 1, res)
    max_depth2, res = determineDepth(root.right, depthSoFar + 1, res)
    print("Node:", root.val)
    print("DSF", depthSoFar)
    print("Max_depth1:", max_depth1, "Max_depth2:", max_depth2)
    res = max(res, max_depth1 + max_depth2)
    return max(max_depth1, max_depth2) + 1, res

