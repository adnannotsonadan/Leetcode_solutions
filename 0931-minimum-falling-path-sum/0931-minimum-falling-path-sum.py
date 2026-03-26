class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        dp=[[None]*n for _ in range(n)]
        def solve(i,j):
            if i>=n or j>=n or j<0:
                return float('inf')
            if i==n-1:
                return matrix[i][j]
            if dp[i][j]!=None:
                return dp[i][j]
            down=matrix[i][j]+solve(i+1,j)
            rdiag=matrix[i][j]+solve(i+1,j+1)
            ldiag=matrix[i][j]+solve(i+1,j-1)
            dp[i][j] = min(down,ldiag,rdiag)
            return dp[i][j]
        
        mini=float('inf')
        for j in range(n):
            mini=min(mini,solve(0,j))
        return mini
        
        