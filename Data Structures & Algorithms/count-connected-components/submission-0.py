class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(set)

        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        all_explored = set()
        cc = 0
        while len(all_explored) < n:
            stack = []
            for i in range(n):
                if i not in all_explored:
                    stack.append(i)
                    break
            explored = set()

            while stack:
                curr = stack.pop()
                explored.add(curr)
                all_explored.add(curr)
                for neighbor in neighbors[curr]:
                    if neighbor not in explored:
                        stack.append(neighbor)
            cc += 1
        return cc