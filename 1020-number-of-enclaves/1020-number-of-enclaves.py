class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])

        def dfs(i, j):
            grid[i][j] = 0
            
            
            if i > 0 and grid[i-1][j] == 1:
                dfs(i-1, j)
            
            if i < n-1 and grid[i+1][j] == 1:
                dfs(i+1, j)
            
            if j > 0 and grid[i][j-1] == 1:
                dfs(i, j-1)
            
            if j < m-1 and grid[i][j+1] == 1:
                dfs(i, j+1)

        for j in range(m):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[n-1][j]==1:
                dfs(n-1,j)
        for i in range(n):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][m-1]==1:
                dfs(i,m-1)
        l=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                # if i!=0 or i!=n-1 or j!=0 or j!=m-1:
                if grid[i][j]==1:
                    l+=1
        return l