class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stack.append(int(token))
            elif token == '+':
                res = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == '-':
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == '*':
                res = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif token == '/':
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
        return stack[-1]
            
            
            
        