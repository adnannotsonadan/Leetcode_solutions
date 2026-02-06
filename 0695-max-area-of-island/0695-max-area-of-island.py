class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        n = len(grid)        
        m = len(grid[0])     
        
        def dfs(i, j):
            grid[i][j] = 0
            area = 1
            
            
            if i > 0 and grid[i-1][j] == 1:
                area += dfs(i-1, j)
            
               
            if i < n-1 and grid[i+1][j] == 1:
                area += dfs(i+1, j)
            
            
            if j > 0 and grid[i][j-1] == 1:
                area += dfs(i, j-1)
            
            
            if j < m-1 and grid[i][j+1] == 1:
                area += dfs(i, j+1)
            
            return area
        
        max_area = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
