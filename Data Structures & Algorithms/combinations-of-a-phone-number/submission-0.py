class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == '':
            return []
        mp = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(s):
            if len(s) >= len(digits):
                res.append(s)
                return
            
            digit = digits[len(s)]
            for c in mp[digit]:
                backtrack(s+c)
                
        backtrack("")
        return res



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