class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        
        def digit(path, used):
            if len(path) == 3:
                if path[-1] % 2 == 0:
                    ans.add(int("".join(map(str, path))))
                return
            
            for i in range(len(digits)):
                if used[i]:
                    continue
                if not path and digits[i] == 0:
                    continue
                
                used[i] = True
                path.append(digits[i])
                
                digit(path, used)
                
                path.pop()
                used[i] = False
        
        digit([], [False]*len(digits))
        return sorted(ans)