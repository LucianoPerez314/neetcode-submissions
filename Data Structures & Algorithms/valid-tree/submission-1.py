class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = defaultdict(set)

        for n1, n2 in edges:
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)

        stack = [(0, None)]
        explored = set()
        
        while stack:
            curr, parent = stack.pop()
            explored.add(curr)
            for neighbor in neighbors[curr]:
                # If we encounter any already visited node that is not the parent of the current node, 
                # we return false as it indicates a cycle. 
                if neighbor in explored:
                    if neighbor != parent:
                        return False
                else:
                    stack.append((neighbor, curr))
        if len(explored) < n:
            return False
        return True
