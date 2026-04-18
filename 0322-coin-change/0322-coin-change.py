class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def rec(ind,amount):
            
            if ind==0:
                if amount%coins[0]==0:
                    return amount//coins[0]
                else:
                    return float('inf')
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            np=0+rec(ind-1,amount)
            take=float('inf')
            if coins[ind]<=amount:
                take=1+rec(ind,amount-coins[ind])
            dp[ind][amount]=min(np,take)
            return dp[ind][amount]
        ans=rec(n-1,amount)
        if ans==float('inf'):
            return -1
        return ans