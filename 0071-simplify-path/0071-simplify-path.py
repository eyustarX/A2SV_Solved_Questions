class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        stack = []

        for i in p:
            if i not in ['','.','..']:
                stack.append(i)
            
            if i == '..' and stack:
                stack.pop()    
        
        return "/" + "/".join(stack)
