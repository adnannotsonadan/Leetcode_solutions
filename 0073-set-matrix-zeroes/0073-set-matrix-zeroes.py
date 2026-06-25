class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        
        def row(r):
            for i in range(m):
                if matrix[r][i]!=0:
                    matrix[r][i]=None
            return
        def col(c):
            for i in range(n):
                if matrix[i][c]!=0:
                    matrix[i][c]=None
            return

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row(i)
                    col(j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] is None:
                    matrix[i][j]=0
        return matrix

        