"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        cloned = {}
        def helper(start):
            clone = Node(start.val, None)
            cloned[start.val] = clone
            for neighbor in start.neighbors:
                if neighbor.val not in cloned:
                    clone_neighbor = helper(neighbor)
                    clone.neighbors.append(clone_neighbor)
                else:
                    clone.neighbors.append(cloned[neighbor.val])
            return clone
        return helper(node)