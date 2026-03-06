class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        prefix = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                s = mat[i][j]

                if i > 0:
                    s += prefix[i-1][j]
                if j > 0:
                    s += prefix[i][j - 1]
                if i > 0 and j > 0:
                    s -= prefix[i - 1][j - 1]
                
                prefix[i][j] = s
        
        ans = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                r1 = max(i - k, 0)
                c1 = max(j - k, 0)
                c2 = min(j + k, m - 1)
                r2 = min(i + k, n -1)

                s = prefix[r2][c2]
                
                if r1 > 0:
                    s -= prefix[r1 - 1][c2]
                if c1 > 0:
                    s -= prefix[r2][c1 -1]
                if r1 > 0 and c1 > 0:
                    s += prefix[r1 - 1][c1 - 1]

                ans[i][j] = s
                
        return ans
                