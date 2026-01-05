class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # board=[]
        # ans=[]
        # row=n
        # col=n
        # for i in range(n):
        #     roww=[]
        #     for j in range(n):
        #         roww.append('.')
        #     board.append(roww)

        # leftRow=[0]*n
        # upperDig=[0]*(2*n-1)
        # lowerDig=[0]*(2*n-1)

        # def solve(col,board,ans,leftRow,upperDig,lowerDig,n):
        #     if col==n:
        #         new_board = []
        #         for row in board:
        #             new_board.append("".join(row))
        #         ans.append(new_board)

        #         return
        #     for i in range(n):
        #         if leftRow[i]==0 and lowerDig[i+col]==0 and upperDig[(n-1)+col-i]==0:
        #             board[i][col]='Q'
        #             leftRow[i]=1
        #             lowerDig[i+col]=1
        #             upperDig[(n-1)+col-i]=1
        #             solve(col+1,board,ans,leftRow,upperDig,lowerDig,n)
        #             board[i][col]='.'
        #             leftRow[i]=0
        #             lowerDig[i+col]=0
        #             upperDig[(n-1)+col-i]=0
        # solve(0,board,ans,leftRow,upperDig,lowerDig,n)
        # return ans
        board=[]
        ans=[]
        for i in range(n):
            r=[]
            for j in range(n):
                r.append('.')
            board.append(r)
        leftRow=[0]*n
        lowerDig=[0]*(2*n-1)
        upperDig=[0]*(2*n-1)

        def solve(col,board,ans,leftRow,lowerDig,upperDig,n):
                if col==n:
                    new_board=[]
                    for row in board:
                        new_board.append("".join(row))
                    ans.append(new_board)
                    return
                for i in range(n):

                    if leftRow[i]==0 and lowerDig[i+col]==0 and upperDig[(n-1)+col-i]==0:
                        board[i][col]='Q'
                        leftRow[i]=1
                        lowerDig[i+col]=1
                        upperDig[(n-1)+col-i]=1
                        solve(col+1,board,ans,leftRow,lowerDig,upperDig,n)
                        board[i][col]='.'
                        leftRow[i]=0
                        lowerDig[i+col]=0
                        upperDig[(n-1)+col-i]=0
        solve(0,board,ans,leftRow,lowerDig,upperDig,n)
        return ans