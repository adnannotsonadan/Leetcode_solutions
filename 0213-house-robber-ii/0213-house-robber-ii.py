class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        def solve(ind,nums,dp):
            if ind<0:
                return 0
            if ind==0:
                return nums[0]
            if dp[ind]!=-1:
                return dp[ind]
            pick=nums[ind]+solve(ind-2,nums,dp)
            np=solve(ind-1,nums,dp)
            dp[ind] = max(pick,np)
            return dp[ind]
        l1=nums[:n-1]
        n1=len(l1)
        l2=nums[1:]
        n2=len(l2)
        dp1=[-1]*n1
        dp2=[-1]*n2
        case1=solve(n1-1,l1,dp1)
        case2=solve(n2-1,l2,dp2)
        return max(case1,case2)
        