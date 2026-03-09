class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {'(':')','[':']','{':'}'}
        stack = []

        for i in range(len(s)):
            if s[i] in my_dict.keys():
                stack.append(s[i])
            
            else:
                if stack and s[i] == my_dict[stack[-1]]:
                    stack.pop()
                
                else:
                    return False
                    
        return True if not stack else False