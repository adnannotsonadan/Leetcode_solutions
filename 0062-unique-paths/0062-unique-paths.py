class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[-1]*n for _ in range(m)]
        def rec(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            left=rec(i-1,j)
            up=rec(i,j-1)
            dp[i][j] = up+left
            return dp[i][j]
        return rec(m-1,n-1)