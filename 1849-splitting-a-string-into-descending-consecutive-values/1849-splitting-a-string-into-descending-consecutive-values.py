class Solution:
    def splitString(self, s: str) -> bool:
        def backtracking(start, path):
            if start == len(s):
                return len(path) > 1
            
            for i in range(start, len(s)):
                curr = int(s[start:i + 1])

                if path:
                    if path[-1] != curr + 1:
                        continue
                    elif curr >= path[-1]:
                        break

                path.append(curr)
                
                if backtracking(i + 1, path):
                    return True
                
                path.pop()
            
            return False
        
        return backtracking(0, [])