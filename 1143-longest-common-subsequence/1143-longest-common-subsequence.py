class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # n=len(text1)
        # m=len(text2)
        # dp=[[-1]*(m+1) for _ in range(n+1)]
        # def rec(ind1,ind2):
        #     if ind1==0 or ind2==0:
        #         return 0
        #     if dp[ind1][ind2]!=-1:
        #         return dp[ind1][ind2]
        #     if text1[ind1-1]==text2[ind2-1]:
        #         dp[ind1][ind2]=1+rec(ind1-1,ind2-1)
        #     else:
        #         dp[ind1][ind2]=max(rec(ind1-1,ind2),rec(ind1,ind2-1))
        #     return dp[ind1][ind2]
        # return rec(n,m)
        
        
        n=len(text1)
        m=len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
        return dp[n][m]