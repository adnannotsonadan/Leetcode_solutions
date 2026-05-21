class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        # n = len(grid)        
        # m = len(grid[0])     
        
        # def dfs(i, j):
        #     grid[i][j] = 0
        #     area = 1
            
            
        #     if i > 0 and grid[i-1][j] == 1:
        #         area += dfs(i-1, j)
            
               
        #     if i < n-1 and grid[i+1][j] == 1:
        #         area += dfs(i+1, j)
            
            
        #     if j > 0 and grid[i][j-1] == 1:
        #         area += dfs(i, j-1)
            
            
        #     if j < m-1 and grid[i][j+1] == 1:
        #         area += dfs(i, j+1)
            
        #     return area
        
        # max_area = 0
        
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 1:
        #             max_area = max(max_area, dfs(i, j))
        
        # return max_area


        n=len(grid)
        m=len(grid[0])
        moves=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j,t):
            vis[i][j]=1
            t+=1
            for dx,dy in moves:
                ni=dx+i
                nj=dy+j
                if ni>=0 and ni<n and nj>=0 and nj<m and vis[ni][nj]==0 and grid[ni][nj]==1:
                    t=dfs(ni,nj,t)
            return t
        tm=0
        # t=0
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1  and not vis[i][j]:
                    t=dfs(i,j,0)
                    tm=max(tm,t)
        return tm



