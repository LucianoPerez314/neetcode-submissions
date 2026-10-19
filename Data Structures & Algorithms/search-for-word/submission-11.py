class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        res = False
        def backtrack(i, xy, prev_xys):
            nonlocal res
            x, y = xy
            # 1. Base Case / Goal Check
            if i == len(word):
                res = True
                return 
            
            choices = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # 2. Iterate through choices at the current decision node
            prev_xys.add(xy)
            for dx, dy in choices:
                # check if coords in bounds
                if x + dx < 0 or x + dx >= cols:
                    continue
                if y + dy < 0 or y + dy >= rows:
                    continue
                
                
                # check that coords is unexplored.
                if (x+dx,y+dy) not in prev_xys and board[y+dy][x+dx] == word[i]:
                    backtrack(i+1, (x+dx, y+dy), prev_xys)
            prev_xys.remove(xy)
        
        for y in range(rows):
            for x in range(cols):
                if board[y][x] == word[0]:
                    backtrack(1, (x, y), set())

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