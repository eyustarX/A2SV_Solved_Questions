class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def dfs(r, c):
            if not inbound(r,c) or board[r][c] != 'O':
                return
            
            board[r][c] = 1

            for dr, dc in direction:
                dfs(r + dr, c + dc) 

        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)

        for i in range(col):
            dfs(0,i)
            dfs(row-1,i)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"  
                elif board[r][c] == 1:
                    board[r][c] = "O"


        
