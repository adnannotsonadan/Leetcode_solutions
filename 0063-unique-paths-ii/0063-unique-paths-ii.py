class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[-1]*(m+1) for _ in range(n)]
        def rec(i,j):
            if i<0 or j<0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            left=rec(i-1,j)
            right=rec(i,j-1)
            dp[i][j]=left+right
            return dp[i][j]
        return rec(n-1,m-1)