class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def dfs(i, visited):
            visited[i] = True
            count = 1
            
            x1, y1, r1 = bombs[i]
            
            for j in range(len(bombs)):
                if not visited[j]:
                    x2, y2, _ = bombs[j]
                    
                    dx = x1 - x2
                    dy = y1 - y2
                    
                    if dx*dx + dy*dy <= r1*r1:
                        count += dfs(j, visited)
            
            return count
        
        ans = 0
        
        for i in range(len(bombs)):
            visited = [False] * len(bombs)
            ans = max(ans, dfs(i, visited))
        
        return ans