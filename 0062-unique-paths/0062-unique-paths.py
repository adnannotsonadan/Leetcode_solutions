class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*n for _ in range(m)]
        def solve(i,j):
            if i==m-1 and j==n-1:
                return 1
            if  i>=m or j>=n:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            down=solve(i+1,j)
            right=solve(i,j+1)
            dp[i][j] = down+right
            return dp[i][j]
        return solve(0,0)