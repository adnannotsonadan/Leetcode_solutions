class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if sum(nums)%2!=0 :
            return False
        t=sum(nums)//2
        dp=[[-1]*(t+1) for _ in range(n+1)]
        def rec(ind,t):
            if ind==len(nums):
                if t==0:
                    return True
                return False
            if dp[ind][t]!=-1:
                return dp[ind][t]
            if nums[ind]<=t:
                inc=rec(ind+1,t-nums[ind])
                    # return True
                ninc=rec(ind+1,t)
                    # return True
                dp[ind][t]=inc or ninc
                return dp[ind][t]
            else:
                dp[ind][t]=rec(ind+1,t)
                return dp[ind][t]
            # return False
        return rec(0,t)
        