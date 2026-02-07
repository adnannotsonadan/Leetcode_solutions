class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[[0]*(n+1) for _ in range(n+1)]
        
        for ind in range(n-1,-1,-1):
            for prev in range(ind-1,-2,-1):
                le=dp[ind+1][prev+1]
                
                if prev==-1 or nums[ind]> nums[prev]:
                    le=max(le,1+dp[ind+1][ind+1])
                dp[ind][prev+1]=le
        return dp[0][0]