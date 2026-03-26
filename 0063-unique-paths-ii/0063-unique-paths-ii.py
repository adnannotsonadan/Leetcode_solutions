class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        i1=None
        j1=None
        dp=[[-1]*m for _ in range(n)]
        if obstacleGrid[n-1][m-1]==1:
            return 0
        def solve(i,j):
            if i==n-1 and j==m-1:
                return 1
            if i>=n or j>=m:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            down=solve(i+1,j)
            right=solve(i,j+1)
            dp[i][j]=down+right
            return dp[i][j]
        return solve(0,0)