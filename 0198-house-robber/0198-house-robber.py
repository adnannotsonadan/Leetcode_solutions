class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*n
        def solve(ind,nums):
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            pick=nums[ind]+solve(ind-2,nums)
            not_pick=solve(ind-1,nums)
            dp[ind] = max(pick,not_pick)
            return dp[ind]
        return solve(n-1,nums)
        