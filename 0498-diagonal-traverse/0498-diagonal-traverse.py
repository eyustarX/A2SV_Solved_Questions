class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        ans = []

        count = n
        for i in range(n+m):
            temp = []
            r = i if i < n else n - 1
            c = 0 if i < n else i - n + 1
            
            while r >= 0  and  c < m:
                temp.append(mat[r][c])
                r -= 1
                c += 1

            if i % 2 == 0:
                ans.extend(temp)
            
            else:
                ans.extend(temp[::-1])
            
        return ans
