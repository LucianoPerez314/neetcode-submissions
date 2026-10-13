class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ')':
                if len(stack) == 0:
                    return False
                foo = stack.pop()
                if foo != '(':
                    return False
            elif c == '}':
                if len(stack) == 0:
                    return False
                foo = stack.pop()
                if foo != '{':
                    return False
            elif c == ']':
                if len(stack) == 0:
                    return False
                foo = stack.pop()
                if foo != '[':
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


        