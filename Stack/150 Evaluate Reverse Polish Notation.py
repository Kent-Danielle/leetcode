class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: int(x/y))}
        res = 0
        stack = []
        # Iterate over the array
        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(token)
            else:
                y = int(stack.pop())
                stack.append(ops[token](int(stack.pop()), y))
        
        return stack.pop()