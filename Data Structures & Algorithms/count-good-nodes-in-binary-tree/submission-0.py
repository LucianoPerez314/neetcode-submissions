# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 2
# 1, 1
# 1, 3
# 1
# 1, 5
# 1
# 

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # approach: depth first search
        # we just check the frontier to see if there is any nodes greater than x in the root.
        traversed = []
        frontier = [(root, root.val)]
        good_nodes = 0
        while len(frontier) != 0:
            current, good_val = frontier.pop()
            if good_val <= current.val:
                good_nodes += 1
            
            if current.left is not None:
                if good_val >= current.left.val:
                    frontier.append((current.left, good_val))
                else:
                    frontier.append((current.left, current.left.val))
            if current.right is not None:
                if good_val >= current.right.val:
                        frontier.append((current.right, good_val))
                else:
                    frontier.append((current.right, current.right.val))
        return good_nodes
            
