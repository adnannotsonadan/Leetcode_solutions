class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*n for _ in range(m)]
        # def solve(i,j):
        #     if i==m-1 and j==n-1:
        #         return 1
        #     if  i>=m or j>=n:
        #         return 0
        #     if dp[i][j]!=0:
        #         return dp[i][j]
        #     down=solve(i+1,j)
        #     right=solve(i,j+1)
        #     dp[i][j] = down+right
        #     return dp[i][j]
        # return solve(0,0)

        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i>0:
                    down=dp[i-1][j]
                else:
                    down=0
                if j>0:
                    right=dp[i][j-1]
                else:
                    right=0
                dp[i][j]=down+right
        return dp[m-1][n-1]
