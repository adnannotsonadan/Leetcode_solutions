class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n=len(text1)
        m=len(text2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        # memo
        # def rec(text1,text2,n,m):
        #     if n==0 or m==0:
        #         return 0
        #     if dp[n][m]!=-1:
        #         return dp[n][m]
        #     if text1[n-1]==text2[m-1]:
        #         dp[n][m]=1 + rec(text1,text2,n-1,m-1)
        #         return dp[n][m]
        #     else:
        #         op1=rec(text1,text2,n,m-1)
        #         op2=rec(text1,text2,n-1,m)
        #         dp[n][m]= max(op1,op2)
        #         return dp[n][m]
        # return rec(text1,text2,n,m)
        # top down
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    op1=dp[i][j-1]
                    op2=dp[i-1][j]
                    dp[i][j]=max(op1,op2)
        return dp[n][m]