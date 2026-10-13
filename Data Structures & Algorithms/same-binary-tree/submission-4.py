# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1 = depthFirstSearch(p)
        l2 = depthFirstSearch(q)
        print("P", l1)
        print("Q", l2)

        if len(l1) != len(l2):
            return False

        for i in range(len(l1)):
            if l1[i] == None or l2[i] == None:
                if l1[i] != l2[i]:
                    return False
                continue
            if l1[i].val != l2[i].val:
                return False 
        return True

def depthFirstSearch(root):
    if root == None:
        return [None]

    path_l = depthFirstSearch(root.left)
    path_r = depthFirstSearch(root.right)

    return [root] + path_l + path_r


        