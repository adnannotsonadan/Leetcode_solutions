class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # n=len(coins)
        # dp=[[0]*(amount+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0]=0
        # for i in range(1,n+1):
        #     for j in range(1,amount+1):
        #         if coins[i-1]<=j:
        #             inc=1+dp[i][j-coins[i-1]]
        #             ninc=dp[i-1][j]
        #             dp[i][j]=min(inc,ninc)
        #         else:
        #             dp[i][j]=dp[i-1][j]
        # return dp[n][amount]









        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def rec(ind,amount):
            if amount==0:
                return 0
            if ind==0:
                if amount%coins[0]==0:
                    return amount//coins[0]
                return float('inf')
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            np=rec(ind-1,amount)
            pick=float('inf')
            if coins[ind]<=amount:
                pick=1+rec(ind,amount-coins[ind])
            dp[ind][amount]=min(pick,np)
            return dp[ind][amount]
        ans=rec(n-1,amount)
        if ans==float('inf'):
            return -1
        return ans













             