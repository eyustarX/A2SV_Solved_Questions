class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                max_value = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        max_value = max(max_value, grid[r][c])
                
                result[i][j] = max_value
        
        return result