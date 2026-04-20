class Solution(object):
    def numIslands(self, grid):
# without visited        
        # if not grid:
        #     return 0
        
        # n = len(grid)        
        # m = len(grid[0])     
        
        # def dfs(i, j):
        #     grid[i][j] = "0"
            
            
        #     if i > 0 and grid[i-1][j] == "1":
        #         dfs(i-1, j)
            
            
        #     if i < n-1 and grid[i+1][j] == "1":
        #         dfs(i+1, j)
            
            
        #     if j > 0 and grid[i][j-1] == "1":
        #         dfs(i, j-1)
            
            
        #     if j < m-1 and grid[i][j+1] == "1":
        #         dfs(i, j+1)
        
        # islands = 0
        
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == "1":
        #             dfs(i, j)
        #             islands += 1
        
        # return islands

# with visited
        # n = len(grid)
        # m = len(grid[0])

        # visited = [[0] * m for _ in range(n)]

        # def dfs(i, j):
        #     visited[i][j] = 1

        #     # up
        #     if i > 0 and grid[i-1][j] == "1" and visited[i-1][j] == 0:
        #         dfs(i-1, j)

        #     # down
        #     if i < n-1 and grid[i+1][j] == "1" and visited[i+1][j] == 0:
        #         dfs(i+1, j)

        #     # left
        #     if j > 0 and grid[i][j-1] == "1" and visited[i][j-1] == 0:
        #         dfs(i, j-1)

        #     # right
        #     if j < m-1 and grid[i][j+1] == "1" and visited[i][j+1] == 0:
        #         dfs(i, j+1)

        # islands = 0

        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == "1" and visited[i][j] == 0:
        #             dfs(i, j)
        #             islands += 1

        # return islands








        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        moves=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j):
            vis[i][j]=1
            for di,dj in moves:
                ni=di+i
                nj=dj+j
                if ni>=0 and ni<n and nj>=0 and nj<m and vis[ni][nj]==0 and grid[ni][nj]=='1':
                    dfs(ni,nj)
        cc=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and vis[i][j]==0:
                    cc+=1
                    dfs(i,j)
        return cc