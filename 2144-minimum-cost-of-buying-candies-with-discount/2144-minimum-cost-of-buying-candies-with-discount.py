class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        cost.sort()
        res=0
        count=0
        i=n-1

        while i>=0:
            res+=cost[i]
            i-=1
            count+=1
            if count==2:
                i-=1
                count=0 
        return res
            