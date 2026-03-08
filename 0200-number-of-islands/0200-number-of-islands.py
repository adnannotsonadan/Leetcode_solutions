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
        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for _ in range(n)]

        def dfs(i, j):
            visited[i][j] = 1

            # up
            if i > 0 and grid[i-1][j] == "1" and visited[i-1][j] == 0:
                dfs(i-1, j)

            # down
            if i < n-1 and grid[i+1][j] == "1" and visited[i+1][j] == 0:
                dfs(i+1, j)

            # left
            if j > 0 and grid[i][j-1] == "1" and visited[i][j-1] == 0:
                dfs(i, j-1)

            # right
            if j < m-1 and grid[i][j+1] == "1" and visited[i][j+1] == 0:
                dfs(i, j+1)

        islands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    dfs(i, j)
                    islands += 1

        return islands