class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Start with an empty adjacency list.
        neighbors = defaultdict(set)

        # Iterate through edges one by one (u, v).
        for a, b in edges:
            # Before adding (u, v) to your graph: check if there is already a path connecting u and v using your current graph.
            if findPath(a, b, neighbors):
                # If a path already connects u to v, adding (u, v) right now will create a cycle. Since you are processing edges in order, this current edge (u, v) is guaranteed to be the redundant edge completing the cycle! 
                return [a, b]
            else: 
                #If no path exists between u and v, add the edge (u, v) to your adjacency list and move to the next edge.
                neighbors[a].add(b)
                neighbors[b].add(a)

            
def findPath(start, end, neighbors):
    stack = [start]
    explored = set()
    while stack:
        curr = stack.pop()
        explored.add(curr)
        for neighbor in neighbors[curr]:
            if neighbor == end:
                return True
            if neighbor not in explored:
                stack.append(neighbor)
            
    return False
        