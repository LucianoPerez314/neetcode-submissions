# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert(root)
        return root
        
def invert(root):
    # Base case
    if root == None:
        return
    # Otherwise recursive case
    invert(root.left), invert(root.right)
    root.left, root.right = root.right, root.left




