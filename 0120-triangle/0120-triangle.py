class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        # m=len(triangle[0])
        dp=[[None]*n for _ in range(n)]
        self.mini=float('inf')
        def solve(i,j):
            if i==n-1 :
                return triangle[i][j]
            if i>=n:
                return float('inf')
            if dp[i][j]!=None:
                return dp[i][j]
            down=solve(i+1,j)
            right=solve(i+1,j+1)
            dp[i][j]=triangle[i][j]+min(down,right)
            return dp[i][j]
        return solve(0,0)
