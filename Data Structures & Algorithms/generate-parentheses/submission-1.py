class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # state = curr_string
        res = []
        def backtrack(p_string):
            print(p_string)
            # Base Case: Since we want n valid pairs then there must be 2 * n characters in the base string.
            if len(p_string) == 2 * n:
                res.append(p_string)
                return
            # At every single step, you are making one decision: Do I place a ( or a ) next?
            l_count, r_count = 0, 0
            for c in p_string:
                if c == "(":
                    l_count += 1
                else:
                    r_count += 1

            # You can always add a ( as long as you haven't reached your maximum budget of open parentheses.
            if l_count < n:
                backtrack(p_string + "(")

            # You can only add a ) if there is at least one unmatched ( already waiting to be closed (i.e., open count $>$ close count).
            if l_count > r_count:
                backtrack(p_string + ")")
            

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