class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # BRUTE FORCE
        # maxi=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]>prices[i]:
        #             x=prices[j]-prices[i]
        #             maxi=max(maxi,x)
        # return maxi

        # OPTIMAL
        # maxi=0
        # mini=float('inf')

        # for i in range(len(prices)):
        #     if prices[i]<mini:
        #         mini=prices[i]
        #     if prices[i]>mini:
        #         maxi=max(maxi,prices[i]-mini)
        # return maxi

        # maxi=0
        # mini=float('inf')

        # for price in prices:
        #     mini=min(mini,price)
        #     if price>mini:
        #         maxi=max(maxi,price-mini)
        # return maxi

        maxi=0
        mini=float('inf')

        for num in prices:
            if num<mini:
                mini=num
            else:
                maxi=max(maxi,num-mini)
        return maxi

