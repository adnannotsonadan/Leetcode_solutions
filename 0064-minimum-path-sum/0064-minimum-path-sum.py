class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*m for _ in range(n)]
        self.mini=float('inf')
        def solve(i,j):
            if i==n-1 and j==m-1:
                return grid[i][j]
            if i>=n or j>=m:
                return float('inf')
            if dp[i][j]!=-1:
                return dp[i][j]
            down=solve(i+1,j)
            right=solve(i,j+1)
            dp[i][j]=grid[i][j]+min(down,right)
            return dp[i][j]
        return solve(0,0)