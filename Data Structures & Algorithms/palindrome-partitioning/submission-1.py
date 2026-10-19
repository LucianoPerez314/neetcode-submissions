class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # Base case. ENd of out partition
            if i >= len(s):
                res.append(part[::])
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
            
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

def backtrack(state, choices):
    # 1. Base Case / Goal Check
    if is_solution(state):
        results.append(state.copy())  # Save a deep copy of the valid state
        return

    # 2. Iterate through choices at the current decision node
    for choice in get_valid_choices(choices, state):
        if is_valid(choice, state):  # Pruning condition
            # --- MAKE CHOICE ---
            state.add(choice)
            
            # --- RECURSE ---
            backtrack(state, remaining_choices)
            
            # --- UNDO CHOICE (BACKTRACK) ---
            state.remove(choice)