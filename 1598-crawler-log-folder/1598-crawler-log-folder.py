class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == "../" and stack:
                stack.pop()
            
            if log != "./" and log != "../":
                stack.append(log)
        
        return len(stack)