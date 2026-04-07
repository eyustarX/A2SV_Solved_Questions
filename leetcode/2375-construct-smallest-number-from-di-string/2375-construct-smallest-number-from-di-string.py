class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        used = [False] * 10
        
        def backtrack(path):
            if len(path) == n + 1:
                return path
            
            for d in range(1, 10):
                if used[d]:
                    continue
                
                if path:
                    if pattern[len(path) - 1] == 'I' and path[-1] >= d:
                        continue
                    if pattern[len(path) - 1] == 'D' and path[-1] <= d:
                        continue
                
                used[d] = True
                res = backtrack(path + [d])
                if res:
                    return res
                used[d] = False
            
            return None
        
        result = backtrack([])
        return "".join(map(str, result))