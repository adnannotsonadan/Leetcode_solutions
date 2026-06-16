class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n=len(nums)
        # dp=[-1]*n
        # dp[0]=nums[0]
        # for i in range(1,n):
        #     if i>1:
        #         pick=nums[i]+dp[i-2]
        #     else:
        #         pick=nums[i]
        #     np=dp[i-1]
        #     dp[i]=max(pick,np)
        # return dp[n-1]

        n=len(nums)
        dp=[-1]*n
        dp[0]=nums[0]
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]
            not_pick=0+dp[i-1]
            dp[i]=max(pick,not_pick)
        return dp[n-1]