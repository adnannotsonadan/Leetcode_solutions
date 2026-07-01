class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        def rec(ind):
            if ind>n:
                return 0
            if ind==n:
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            one=rec(ind+1)
            two=rec(ind+2)
            dp[ind]=one + two
            return dp[ind]
        return rec(0)
        