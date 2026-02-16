class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r,c = rStart,cStart
        ans = [[r,c]]
        total = rows * cols
        steps = 1

        while len(ans) < total:
            # east
            for i in range(steps):
                c += 1
                if 0 <= c < cols and 0 <= r < rows:
                    ans.append([r,c])
            
            # south
            for i in range(steps):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r,c])
            steps += 1

            # west
            for i in range(steps):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r,c])
            
            # north
            for i in range(steps):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r,c])
            steps += 1

            
        return ans
