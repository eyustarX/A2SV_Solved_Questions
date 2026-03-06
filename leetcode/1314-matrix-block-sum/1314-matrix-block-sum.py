class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                s = 0
                for a in range(i - k, i + k + 1):
                    if a < 0 or a >= n:
                        continue
                    for b in range(j - k, j + k + 1):
                        if b >= 0 and b < m:
                            s += mat[a][b]
                ans[i][j] = s
        
        return ans