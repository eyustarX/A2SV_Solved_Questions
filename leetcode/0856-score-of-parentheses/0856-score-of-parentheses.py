class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            
            elif stack:
                k = stack.pop()
                stack[-1] += max(1, k * 2)
                
        return stack[-1]