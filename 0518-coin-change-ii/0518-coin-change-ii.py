class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        # n = len(coins)
        # dp = [[0] * (amount + 1) for _ in range(n + 1)]

        
        # for i in range(n + 1):
        #     dp[i][0] = 1

        # for i in range(1, n + 1):
        #     for j in range(1, amount + 1):
        #         if coins[i-1] <= j:
        #             inc = dp[i][j - coins[i-1]]   
        #             ninc = dp[i-1][j]
        #             dp[i][j] = inc + ninc
        #         else:
        #             dp[i][j] = dp[i-1][j]

        # return dp[n][amount]

        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def rec(ind,amount):
            if amount==0:
                return 1
            if ind==0:
                if amount%coins[0]==0:
                    return 1
                return 0
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            np=rec(ind-1,amount)
            p=0
            if coins[ind]<=amount:
                p=rec(ind,amount-coins[ind])
            dp[ind][amount]=p+np
            return dp[ind][amount]
        return rec(n-1,amount)        