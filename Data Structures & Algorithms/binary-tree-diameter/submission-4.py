# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = determineDepth(root, 0)
        return diameter

def determineDepth(root, res):
    if root is None:
        return 0, res  # return both depth and current res

    left_depth, res = determineDepth(root.left, res)
    right_depth, res = determineDepth(root.right, res)

    # update the res at this node
    res = max(res, left_depth + right_depth)

    # return depth of this node + updated res
    return max(left_depth, right_depth) + 1, res


