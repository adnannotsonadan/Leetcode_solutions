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
                matrix[r][i]=0
            return
        def col(c):
            for i in range(n):
                matrix[i][c]=0
            return

        d=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    d.add((i,j))
        for i in range(len(d)):
            r,c=d.pop()
            row(r)        
            col(c)

        