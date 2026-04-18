class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # n=len(coins)
        # dp=[[-1]*(amount+1) for _ in range(n)]
        # def rec(ind,amount):
        #     if amount==0:
        #         return 0
        #     if ind==0:
        #         if amount%coins[0]==0:
        #             return amount//coins[0]
        #         else:
        #             return float('inf')
        #     if dp[ind][amount]!=-1:
        #         return dp[ind][amount]
        #     np=0+rec(ind-1,amount)
        #     take=float('inf')
        #     if coins[ind]<=amount:
        #         take=1+rec(ind,amount-coins[ind])
        #     dp[ind][amount]=min(np,take)
        #     return dp[ind][amount]
        # ans=rec(n-1,amount)
        # if ans==float('inf'):
        #     return -1
        # return ans


        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]

        for i in range(0,amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float('inf')
            
        for ind in range(1,n):
            for amt in range(amount+1):
                np=0+dp[ind-1][amt]
                p=float('inf')
                if coins[ind]<=amt:
                    p=1+dp[ind][amt-coins[ind]]
                dp[ind][amt]=min(p,np)
        ans=dp[n-1][amount]
        if ans==float('inf'):
            return -1
        return ans
            