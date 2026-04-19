class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for _ in range(n)]
        def rec(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2]=1+rec(ind1-1,ind2-1)
            if text1[ind1]!=text2[ind2]:
                dp[ind1][ind2]=max(rec(ind1-1,ind2),rec(ind1,ind2-1))
            return dp[ind1][ind2]
        return rec(n-1,m-1)