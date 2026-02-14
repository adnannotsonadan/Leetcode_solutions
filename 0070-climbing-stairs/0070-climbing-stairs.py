class Solution(object):
    def climbStairs(self, n):
        dp=[-1]*(n+1)
        def rec(ind):
            if ind==0:
                return 1
            if ind==1:
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            left=rec(ind-1)
            right=rec(ind-2)
            dp[ind] = right+left 
            return dp[ind]
        return rec(n)