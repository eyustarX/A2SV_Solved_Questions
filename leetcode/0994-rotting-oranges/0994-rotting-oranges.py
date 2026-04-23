class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        fresh = time = 0

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r,c])
        
        while queue and fresh:
            for _ in range(len(queue)):
                r, c  = queue.popleft()
                flag = False

                for dr, dc in directions:
                    if inbound(r + dr, c + dc) and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        queue.append([r + dr, c + dc])
                        fresh -= 1
            
            time += 1

        return time if fresh == 0 else -1
            