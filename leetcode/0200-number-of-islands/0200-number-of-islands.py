class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = [[False for _ in range(col)] for _ in range(row)]

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == "0" or visited[r][c]:
                return

            visited[r][c] = True

            for dr,dc in directions:
                dfs(r + dr, c + dc)
            
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    count += 1
        
        return count