class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False for _ in range(col)] for _ in range(row)]

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col

        def dfs(r,c):
            perimeter = 0
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc):
                    perimeter += 1
                
                elif grid[nr][nc] == 0:
                    perimeter += 1
                
                elif not visited[nr][nc]:
                    perimeter += dfs(nr, nc)
            
            return perimeter
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r,c)
            
        return 0
