class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols = set()
        main_d = set()
        anti_d = set()
        ans = []

        def backtracking(row):
            if row == n:
                ans.append(["".join(r) for r in board])


            for col in range(n):
                if col in cols or row - col in main_d or row + col in anti_d:
                    continue

                cols.add(col)
                main_d.add(row - col)
                anti_d.add(row + col)
                board[row][col] = 'Q'

                backtracking(row + 1)

                cols.remove(col)
                main_d.remove(row - col)
                anti_d.remove(row + col)
                board[row][col] = '.'
            
        backtracking(0)

        return ans