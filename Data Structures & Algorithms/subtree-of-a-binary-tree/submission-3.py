# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_traversed = depthFirstSearch(root)
        sub_traversed = depthFirstSearch(subRoot)
        for node in root_traversed:
            if node == None:
                continue
            if self.isSameTree(node, sub_traversed):
                return True
        print("YO?")
        return False

    def isSameTree(self, p: Optional[TreeNode], already_traversed) -> bool:
        l1 = depthFirstSearch(p)
        l2 = already_traversed

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

        