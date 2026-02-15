class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m = 0
        k = len(mat)

        if mat == target:
            return True

        while m < 3:
            for i in range(k // 2):
                for j in range(i, k - 1 - i):
                    r, c = i, j
                    r1, c1 = c, k - 1 - r
                    r2, c2 = c1, k - 1 - r1
                    r3, c3 = c2, k - 1 - r2

                    mat[r][c], mat[r1][c1], mat[r2][c2], mat[r3][c3] = mat[r3][c3], mat[r][c], mat[r1][c1], mat[r2][c2]

            if mat == target:
                return True

            m += 1

        return False