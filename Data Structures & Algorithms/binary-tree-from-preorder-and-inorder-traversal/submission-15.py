# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = [-1]
        inorder_map = {val: index for index, val in enumerate(inorder)}
        # Preorder: Root → Left → Right
        # Inorder: Left -> Root -> Right
        def helper(left_bound, right_bound):
            i[0] += 1
            if i[0] >= len(preorder):
                return None
            root_val = preorder[i[0]]
            curr = TreeNode(root_val, None, None)

            #root_idx = io.index(root_val)
            root_idx = inorder_map[root_val]
            

            #left_sub = io[:root_idx]
            # if len(left_sub) != 0:
                #curr.left = helper(left_sub)
            if left_bound <= root_idx - 1:
                curr.left = helper(left_bound, root_idx-1)

            # right_sub = io[root_idx+1:]
            # if len(right_sub) != 0:
                #curr.right = helper(right_sub)
            if root_idx + 1 <= right_bound:
                curr.right = helper(root_idx+1, right_bound)

            return curr



        return helper(0, len(inorder))




