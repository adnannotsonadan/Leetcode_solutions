class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                elif board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        for j in range(9):
            s=set()
            for i in range(9):
                if board[i][j]=='.':
                    continue
                elif board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        def traversal(grid,sr,sc,er,ec):
            s=set()
            for i in range(sr,er+1):
                for j in range(sc,ec+1):
                    if board[i][j]=='.':
                        continue
                    elif board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])

        for sr in range(0,9,3):
            er=sr+2
            for sc in range(0,9,3):
                ec=sc+2
                if traversal(board,sr,sc,er,ec)==False:
                    return False
        return True
        

