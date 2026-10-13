# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find first part where the path splits when searching
        
        # recursive approach:
        ## base case (if p or q is the root):
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        
        # base case (if p and q are in different subtrees from the root)
        if p.val < root.val and q.val > root.val:
            return root
        if q.val < root.val and p.val > root.val:
            return root
        
        # recursive case (p and q are both either left or right subtree)
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        