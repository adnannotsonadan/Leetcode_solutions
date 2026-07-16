class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    s.append((i,j))
        while s:
            x,y=s.pop()
  
            for i in range(n):
                matrix[x][i]=0
            for j in range(m):
                matrix[j][y]=0
                # print(j)
        return matrix
