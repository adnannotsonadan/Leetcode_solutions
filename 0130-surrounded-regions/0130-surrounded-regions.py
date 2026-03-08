class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # grid = board[:]
        n=len(board)
        m=len(board[0])
        def dfs(i,j):
            board[i][j]='#'
            # up
            if i>0 and board[i-1][j]=='O':
                dfs(i-1,j)
            # down
            if i<n-1 and board[i+1][j]=='O':
                dfs(i+1,j)
            # left
            if j>0 and board[i][j-1]=='O':
                dfs(i,j-1)
            # right
            if j<m-1 and board[i][j+1]=='O':
                dfs(i,j+1)
        for j in range(m):
            if board[0][j]=='O':
                dfs(0,j)
            if board[n-1][j]=='O':
                dfs(n-1,j)
        for i in range(n):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][m-1]=='O':
                dfs(i,m-1)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    # dfs(i,j)
                    board[i][j]='X'
                if board[i][j]=='#':
                    board[i][j]='O'
        return board
                    
        