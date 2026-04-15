class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtracking(start, path):
            if start == len(num):
                return len(path) >= 3

            
            for i in range(start, len(num)):
                if num[start] == '0' and i > start:
                    break
                
                curr = int(num[start:i + 1])
                if len(path) > 1:
                    if curr < path[-1] + path[-2]:
                        continue
                    
                    elif curr > path[-1] + path[-2]:
                        break
                    
                path.append(curr)

                if backtracking(i+1,path):
                    return True
                
                path.pop()
                
            return False
            
        return backtracking(0,[])
