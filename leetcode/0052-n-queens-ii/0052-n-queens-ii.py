class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        cols = set()
        main_d = set()
        anti_d = set()
        self.count = 0

        def backtracking(row):
            if row == n:
                self.count += 1
                return
            
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

        return self.count