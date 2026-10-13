# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1
# 2, 3
# 3, 4, 5
# 4, 5, 6, 7
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        traversed = []
        # each entry stores the node and its distance from the root.
        frontier = [(root, 0)]
        res = [[]]
        curr_lvl = 0
        while True:
            curr, root_dist = frontier.pop(0)
            
            if curr.left is not None:
                frontier.append((curr.left, root_dist+1))
            if curr.right is not None:
                frontier.append((curr.right, root_dist+1))

            if root_dist == curr_lvl:
                res[curr_lvl].append(curr.val)
            else:
                curr_lvl += 1
                res.append([])
                res[curr_lvl].append(curr.val)

            if len(frontier) == 0:
                break

        return res


        