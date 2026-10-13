# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, isBalanced = checkBalance(root, True)
        return isBalanced

def checkBalance(root, res):
    if root == None or res == False:
        return 0, res

    left_height, res1 = checkBalance(root.left, res)
    right_height, res2 = checkBalance(root.right, res)
    if abs(left_height - right_height) > 1 or res1 == False or res2 == False:
        return 0, False

    return max(left_height, right_height) + 1, res

        